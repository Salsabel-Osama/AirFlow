from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime
import random

def welcome_message():
    print("Welcome! My name is Salsabel Osama")

def generate_random():
    number = random.randint(1, 100)
    with open("/tmp/random.txt", "w") as f:
        f.write(str(number))
    print(f"Random number {number} saved to /tmp/random.txt")

with DAG(
    dag_id="Airflow_Depi",
    start_date=datetime(2025, 10, 3),
    schedule_interval=None,  
    catchup=False
) as dag:

    # Task 1: Print current date
    task1 = BashOperator(
        task_id="print_date",
        bash_command="date"
    )

    # Task 2: Print welcome message
    task2 = PythonOperator(
        task_id="print_welcome",
        python_callable=welcome_message
    )

    # Task 3: Generate random number
    task3 = PythonOperator(
        task_id="generate_random_number",
        python_callable=generate_random
    )

    #  task1 → task2 → task3
    task1 >> task2 >> task3
