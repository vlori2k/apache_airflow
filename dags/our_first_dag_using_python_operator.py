from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.python import PythonOperator


def hello_with_ti_xcoms(age, ti):
    first_name = ti.xcom_pull(task_ids='get_name_ti_mode', key='first_name')
    last_name = ti.xcom_pull(task_ids='get_name_ti_mode', key='last_name')
    print(f"Hello hello! my name is {first_name} {last_name} and i am {age} years old!")


def get_name_ti_mode(ti):
    ti.xcom_push(key="first_name", value="vlorjanovic")
    ti.xcom_push(key="last_name", value="badallajovic")


def hello(name : str, age : int):
    print(f"Hello, my name is: {name}, and i am {age} years old")


def get_name_vlori():
    return 'vlori'




default_args = {
    'owner': 'Vlorjan',
    'retries': 3,
    'retry_delay': timedelta(minutes=5)
}


with DAG(
    dag_id='our_dag_with_python_operator12',
    description='Here we are creating our first DAG with python operator',
    start_date=datetime(2021, 1, 1),
    schedule='@daily',
    default_args=default_args,
    catchup=False

) as dag:


    task1 = PythonOperator(
        task_id='hvaskjerda',
        python_callable=hello_with_ti_xcoms,

        op_kwargs={'age': 28},
    )


    task2 = PythonOperator(

        task_id='task2_vlori_09',
        python_callable=get_name_vlori,

    )

    task2 >> task1