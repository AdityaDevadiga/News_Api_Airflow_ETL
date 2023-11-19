from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from news_api_etl import fetch_news_headlines

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 11, 19),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'newsapi_dag',
    default_args=default_args,
    description='DAG for fetching news headlines and uploading to S3!',
    schedule_interval=timedelta(days=1),
)

run_etl_newsapi = PythonOperator(
    task_id='complete_newsapi_etl',
    python_callable=fetch_news_headlines,
    dag=dag,
)

run_etl_newsapi