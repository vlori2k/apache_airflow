from datetime import datetime, timedelta

import boto3
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator


default_args = {
    'owner': 'Vlorjan',
    'retries': 3,
    'retry_delay': timedelta(minutes=5)
}


with DAG(
    dag_id='dag_with_s3_bucket_v01',
    start_date=datetime(2025, 4, 22),
    schedule='@daily',
    default_args=default_args,
    catchup=False,
) as dag:
    pass