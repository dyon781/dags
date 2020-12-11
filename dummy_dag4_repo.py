from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime
with DAG('dummy_dag4', start_date=datetime(2019, 1, 1)) as dag:
    op = DummyOperator1(task_id='op')