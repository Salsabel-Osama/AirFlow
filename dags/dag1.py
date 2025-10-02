from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

with DAG(
    dag_id="my_first_dag",
    start_date=datetime(2025, 9, 28),
    schedule_interval=timedelta(minutes=1),
    catchup=False
) as dag:
   task_hello = BashOperator(
       task_id="task_hello",
       bash_command='echo "My name is Salsabel"'
   )

task_hello