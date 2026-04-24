
from dag_controller import DagController


a_dag = DagController()
a_dag.set_datetime_for_task(2024, 4, 23)

a_dag.dag_settings.create_default_args("qazimo", 3, 44)
a_dag.generate_dag("HAHAHA")



