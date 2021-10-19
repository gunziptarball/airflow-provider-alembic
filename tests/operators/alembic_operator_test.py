import airflow.hooks.dbapi
import alembic.command
import hamcrest as ham
import pytest

from alembic_provider.operators.alembic_operator import (
    AlembicBaseOperator,
    AlembicUpgradeOperator,
)


class TestBaseAlembicOperator:
    conn_id = "some_connection_id"

    @pytest.fixture
    def script_location(self, project_root):
        return str(project_root / "migrations/versions")

    @pytest.fixture
    def task(self, script_location):
        return AlembicBaseOperator(
            task_id="foobar",
            conn_id=self.conn_id,
            script_location=script_location,
        )

    @pytest.fixture
    def hook(self, mocker, when):
        m = mocker.Mock()
        when(airflow.hooks.dbapi).DbApiHook(self.conn_id).thenReturn(m)
        return m

    def test_get_config(self, task, when, hook, script_location):
        cfg = task.get_config()
        ham.assert_that(
            cfg.get_main_option("sqlalchemy.url"),
            ham.equal_to(str(hook.get_sqlalchemy_engine.return_value.url)),
        )
        ham.assert_that(
            cfg.get_main_option("script_location"),
            ham.equal_to(script_location),
        )


class TestAlembicUpgradeOperator:
    def test_execute(self, when, mocker):
        cfg = mocker.Mock()
        task = AlembicUpgradeOperator(
            task_id="upgrade_db",
            conn_id="some_connection",
            script_location="some/location",
            revision="ae1234",
        )
        when(task).get_config().thenReturn(cfg)
        when(alembic.command).upgrade(cfg, "ae1234")
        task.execute({})
