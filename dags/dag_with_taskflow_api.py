from datetime import datetime, timedelta

from airflow.decorators import dag, task


default_args = {
    'owner': 'Vlorjan',
    'retries': 3,
    'retry_delay': timedelta(minutes=5)
}


@dag(
    dag_id='dag_with_taskflow_api_v01',
    default_args=default_args,
    start_date=datetime(2026, 4, 19),
    schedule='@daily',
    catchup=False,
)




def hello_world_etl():

    @task()
    def get_name():
        return 'vlorjan'

    def get_age():
        return '33'

    @task()
    def greet(name, age):
        print(f"Hello, my name is {name}, and I am {age} years old!")

    name = get_name()
    age = get_age()

    greet(name=name, age=age)


greet_dag = hello_world_etl()