from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator


class DagSettings:

    def __init__(self):

        self.owner_name = 'no_owned_speficied'

        self.retries = 4

        self.retry_delay = timedelta(minutes=6)

        self.default_args = {
            'owner': self.owner_name,
            'retries': self.retries,
            'retry_delay': self.retry_delay,
        }


    def set_retries(self, retries: int) -> None:
        self.retries = retries
        self.dag_settings.default_args['retries'] = self.retries

    def create_default_args(self, name: str, retries: int, retry_delay: int) -> dict:
        self.owner_name = name
        self.retries = retries
        self.retry_delay = timedelta(minutes=retry_delay)


        self.default_args = {
            'owner': self.owner_name,
            'retries': self.retries,
            'retry_delay': self.retry_delay,
        }

        return self.default_args


    def get_default_args(self):
        return self.default_args