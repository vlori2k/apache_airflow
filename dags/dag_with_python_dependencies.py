from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.providers.standard.operators.python import PythonOperator

default_args = {
    'owner': 'Vlorjan',
    'retries': 3,
    'retry_delay': timedelta(minutes=5)
}

def get_sklearn():
    import sklearn
    print(f"scikit-learn with version: {sklearn.__version__}")

with DAG(
    dag_id='dag_with_python_dependencies_v01',
    default_args=default_args,
    start_date=datetime(2026, 4, 22),
    schedule='@daily',

) as dag:

    get_sklearn = PythonOperator(
        task_id='get_sklearn',
        python_callable=get_sklearn,

    )

    get_sklearn