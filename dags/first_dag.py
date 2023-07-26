from airflow.models import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

from airflow.operators.dummy import DummyOperator

import utility as util

default_arguments = {
    'owner': 'Jay',
    'retries': 1,
    'retry_delay': timedelta(minutes=10)
}

with DAG(
        dag_id='first_dag',
        start_date=datetime(2023, 7, 24),
        default_args=default_arguments
) as dag:
    begin, end = [DummyOperator(task_id=x) for x in ['begin', 'end']]


    def print_something(something):
        print(something)


    task1 = PythonOperator(
        task_id='task1',
        python_callable=print_something,
        op_kwargs={'something': 'abc'}
    )

    bash_task = BashOperator(
        task_id="bash_task",
        bash_command=f'Rscript {util.scripts_path}/rscripts/test_r_script.R',
    )

    begin >> task1 >> bash_task >> end
