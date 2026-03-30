import pandas as pd 
from sqlalchemy import create_engine

URL = "postgresql://postgres:postgrespasswd@localhost:5432/postgres"

df = pd.read_csv("data_kategorik.csv", encoding='windows-1252')

engine = create_engine(URL)
df.to_sql('students', engine, if_exists='replace', index=False)