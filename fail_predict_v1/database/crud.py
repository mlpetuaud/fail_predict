import pandas as pd
import settings
import models
import prepare_dataset
import sqlalchemy
#from sqlalchemy import create_engine, BigInteger, String


def recreate_database():
    models.Base.metadata.drop_all(engine)
    models.Base.metadata.create_all(engine)


def create_dataset_table():
    dataset = pd.read_csv(f"{prepare_dataset.data_path}/total_2018.csv")
    dataset = prepare_dataset.add_custom_cols(dataset)
    dataset = prepare_dataset.rename_cols(dataset)
    dtypes_dict = prepare_dataset.get_dataset_dtype_dict(dataset)
    dataset.to_sql('dataset', engine, if_exists='replace', index=False, dtype = dtypes_dict)
    #add_pk("dataset", "SIRET")


def add_pk(table_name, column_name):
    engine.execute(f"ALTER TABLE {table_name} ADD CONSTRAINT {column_name}_pk PRIMARY KEY ({column_name});")

def create_naf_table():
    naf = pd.read_excel(f"{prepare_dataset.data_path}/table_NAF2-NA.xls", header=[1])
    naf = prepare_dataset.prepare_naf_df(naf)
    naf = prepare_dataset.rename_cols(naf)
    dtypes_dict = prepare_dataset.get_dataset_dtype_dict(naf)
    naf.to_sql('naf', engine, dtype=dtypes_dict)
    #add_pk("naf", "Code APE")

def create_users_table():
    engine.execute(f"""CREATE TABLE IF NOT EXISTS users
    (userid SERIAL PRIMARY KEY,
    username VARCHAR,
    password VARCHAR);
    """)

def drop_table(table_name):
    engine.execute(f"DROP TABLE IF EXISTS {table_name};")

def clear_db():
    engine.execute("DROP SCHEMA public CASCADE;")
    engine.execute("CREATE SCHEMA public;")

def create_db():
    create_dataset_table()
    create_naf_table()
    create_users_table()
    

engine = sqlalchemy.create_engine(settings.DATABASE_URI, echo=True)
#clear_db()
#create_db()

drop_table("users")
create_users_table()


result_set = engine.execute("SELECT * FROM information_schema.tables;")
for r in result_set:  
    print(r)
