# importando as bibliotecas e métodos necessários
import pandas as pd
import requests as req
from google.cloud.bigquery import dataset
from google.cloud import bigquery
from datetime import datetime

# definino o nome do dataset e da tabela
gcp_project = 'match-datastudio'
bq_dataset = 'dados_ip_nestle_ds_link'

client = bigquery.Client(project=gcp_project)
dataset_ref = client.dataset(bq_dataset)

# função que executará as nossas queries
def executa_query(sql):
    query = client.query(sql)
    results = query.result()
    return results.to_dataframe()
