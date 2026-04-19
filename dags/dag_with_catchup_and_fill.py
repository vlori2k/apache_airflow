from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

default_args = {
    'owner': 'Vlorjan',
    'retries': 3,
    'retry_delay': timedelta(minutes=5)
}

"""
with DAG(
    dag_id='dag_with_catchio_backfill_v02',
    default_args=default_args,
    start_date=datetime(2026, 4, 18),
    schedule='@daily',
    catchup=True
) as dag:

    task1 = BashOperator(
        task_id='task2',
        bash_command='echo hahahahahahahahahahahaha This is a simple bash command!'
    )
"""


# med catchup False
with DAG(
    dag_id='dag_with_catchio_backfill_v03',
    default_args=default_args,
    start_date=datetime(2026, 4, 18),
    schedule='@daily',
    catchup=False
) as dag:

    task1 = BashOperator(
        task_id='task3',
        bash_command='echo hahahahahahahahahahahaha This is a simple bash command!'
    )