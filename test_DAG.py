from airflow import DAG
from airflow.providers.http.operators.http import HttpOperator
import datetime

FILENAME = "C:\semester 4\data eng\lab\Job1.kjb"

with DAG(
    dag_id = "test_DAG",
    start_date=datetime.datetime(2026, 5, 27),
    schedule_interval="@daily",
    catchup=False
)as dag:
    run_job=HttpOperator(
        task_id="run_job",
        http_conn_id="carte_conn",
        endpoint="kettle/executeJob",
        data={
            'job': FILENAME
        },
        method="GET"
    )