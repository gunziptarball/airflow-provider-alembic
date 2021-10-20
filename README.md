## Alembic Operators for Airflow

This project defines an operator for [Alembic](https://pypi.org/project/alembic/) for [Apache Airflow](https://airflow.apache.org/). The aim is to provide the ability to include Alembic functionality within an Apache DAG.
The current implementation of Alembic operators includes:

- `AlembicBaseOperator` - Provides DAG node for Airflow
- `AlembicUpgradeOperator` - Wraps `alembic.command.upgrade` 


### Development

- Install dev dependencies: `pip install -r requirements-dev.txt`
- Run tests: `make test` or `pytest tests` 
- Prettify code (using [Black](https://pypi.org/project/black/)): `make pretty`
