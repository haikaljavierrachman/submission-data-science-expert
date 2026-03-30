import pandas as pd 
from sqlalchemy import create_engine

URL = "postgresql://postgres:postgrespasswd@localhost:5432/postgres"

df = pd.read_csv("employee_data.csv", encoding='windows-1252')

engine = create_engine(URL)
df.to_sql('employees', engine, if_exists='replace', index=False)