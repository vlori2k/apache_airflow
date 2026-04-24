from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator


class DagScheduler:

    def __init__(self):

        self.number_of_tasks = 1
        self.tasks_order = []  # for instance, if list is : [task1, task3, task2], then the order will be: task1 before task3, and task3 before task 2.  Maybe we should have a dict because some tasks can run together at once?
