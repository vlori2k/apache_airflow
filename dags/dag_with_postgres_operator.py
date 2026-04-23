from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator

default_args = {
    'owner': 'Vlorjan',
    'retries': 3,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='dag_with_postgres_operator_v015',
    default_args=default_args,
    start_date=datetime(2026, 4, 20),
    schedule='0 0 * * *',
    catchup=False,
) as dag:

    task1 = SQLExecuteQueryOperator(
        task_id='create_postgres_table',
        conn_id='postgres_localhost',
        sql="""
        CREATE TABLE IF NOT EXISTS dag_runs (
            dt DATE,
            dag_id CHARACTER VARYING,
            PRIMARY KEY (dt, dag_id)
        )
        """,
    )

    task2 = SQLExecuteQueryOperator(
        task_id='insert_into_table',
        conn_id='postgres_localhost',
        sql="""
        INSERT INTO dag_runs (dt, dag_id)
        VALUES ('{{ ds }}', '{{ dag.dag_id }}')
        """,
    )

    task1 >> task2