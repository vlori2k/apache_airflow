from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator


default_args = {
    'owner': 'Vlorjan',
    'retries': 3,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='dag_with_cron_expression_v01',
    default_args=default_args,
    start_date=datetime(2026, 4, 15),
    schedule='@daily'


) as dag:
    task1 = BashOperator(
        task_id='cron_task1',
        bash_command='echo "dag with cron expression"'
    )