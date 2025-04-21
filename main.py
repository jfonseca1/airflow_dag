from airflow.models.dag import DAG
from datetime import datetime

with DAG("d1", 
         description="",
         schedule_interval="@daily",
         start_date=datetime(2024,1,1),
         catchup=False):
    pass
