from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator


default_args = {
    'owner': 'Vlorjan',
    'retries': 3,
    'retry_delay': timedelta(minutes=5)
}


with DAG(
    dag_id='first_dag_eksempel2',
    description='First DAG',
    start_date=datetime(2021, 1, 1),
    schedule='@daily',
    default_args=default_args,
    catchup=False


) as dag:

    task1 = BashOperator(
        task_id='task1',
        bash_command='echo "Dette er første dag, bra jobba Vlorjan, du lærte dette fort!"',
    )

    task2 = BashOperator(
        task_id='task2',
        bash_command='echo "hey jeg er task 2, jeg skal kjøre etter task 1"',
    )

    task3 = BashOperator(
        task_id='task3',
        bash_command='echo "hey jeg er task 3, jeg skal kjøre etter task 1 samtidig som task 2!"',
    )

    task1 >> [task2, task3]