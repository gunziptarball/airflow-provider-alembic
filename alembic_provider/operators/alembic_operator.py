from typing import Any, Dict

import alembic.command
import alembic.config
from airflow.hooks import dbapi
from airflow.models import BaseOperator


class AlembicBaseOperator(BaseOperator):
    template_fields = ("conn_id", "script_location", "revision")
    # TODO: someone with better taste in colors please help here
    ui_color = "#aee883"

    def __init__(
        self,
        *,
        conn_id: str,
        script_location: str,
        **kwargs: Any,
    ) -> None:
        self.conn_id = conn_id
        self.script_location = script_location

        super().__init__(**kwargs)

    def get_config(self) -> alembic.config.Config:
        hook = dbapi.DbApiHook(self.conn_id)
        url = hook.get_sqlalchemy_engine().url

        cfg = alembic.config.Config()
        cfg.set_main_option("sqlalchemy.url", str(url))
        cfg.set_main_option("script_location", str(self.script_location))
        return cfg

    def execute(self, context: Dict[str, Any]) -> Any:
        raise NotImplementedError


class AlembicUpgradeOperator(AlembicBaseOperator):
    template_fields = AlembicBaseOperator.template_fields + ("revision",)

    def __init__(self, *, revision: str, **kwargs):
        self.revision = revision
        super().__init__(**kwargs)

    def execute(self, context):
        alembic.command.upgrade(self.get_config(), self.revision)
