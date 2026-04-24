from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

from dag_settings import DagSettings


class DagController:
    def __init__(self):
        self.owner_name = 'airflow'
        self.retries = 4
        self.retry_delay = timedelta(minutes=6)



        self.year = datetime.now().year
        self.month = datetime.now().month
        self.day = datetime.now().day

        self.catchup = False  # hopper over gamle schedulede kjøringer
        self.schedule = '@daily'
        self.schedules_list = ['@once', '@hourly', '@daily', '@weekly', '@monthly', '@yearly']

        self.bash_command = 'echo "dag with cron expression"'

        self.dag_settings = DagSettings()



    def set_schedule(self, schedule: str) -> None:
        self.schedule = schedule


    def set_datetime_for_task(self, year: int, month: int, day: int) -> None:
        self.year = year
        self.month = month
        self.day = day

    def define_schedule(self, schedule: str) -> None:
        if schedule not in self.schedules_list:
            self.schedule = '@daily'
        else:
            self.schedule = schedule



    def generate_dag(self, dag_id: str) -> DAG:
        with DAG(
            dag_id=dag_id,
            default_args=self.dag_settings.default_args,
            start_date=datetime(self.year, self.month, self.day),
            schedule=self.schedule,
            catchup=self.catchup,

        ) as dag:

            BashOperator(
                task_id='task1',
                bash_command=self.bash_command,
            )

        return dag

