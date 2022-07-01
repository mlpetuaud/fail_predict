import pandas as pd
import settings
import prepare_dataset
import sqlalchemy
#from sqlalchemy import create_engine, BigInteger, String


def add_fk(table_from, column_name, table_to):
    engine.execute(f"""ALTER TABLE {table_to} ADD CONSTRAINT {column_name}_fk 
        FOREIGN KEY ({column_name}) REFERENCES {table_from} ({column_name});""")


def add_pk(table_name, column_name):
    engine.execute(f"""ALTER TABLE {table_name} ADD CONSTRAINT {column_name}_pk 
        PRIMARY KEY ({column_name});""")

def clear_db():
    engine.execute("DROP SCHEMA public CASCADE;")
    engine.execute("CREATE SCHEMA public;")


def create_dataset_table():
    """This function creates in DB the table named 'dataset' and fills it with relevant data
    """    
    dataset = pd.read_csv(f"{prepare_dataset.data_path}/total_2018.csv")
    dataset = dataset.drop_duplicates()
    dataset = prepare_dataset.add_custom_cols(dataset)
    dataset = prepare_dataset.rename_cols(dataset)
    dtypes_dict = prepare_dataset.get_dataset_dtype_dict(dataset)
    dataset.to_sql('dataset', engine, if_exists='replace', index=False, dtype = dtypes_dict)
    add_pk('dataset', 'siret')
    add_fk('naf', 'code_ape', 'dataset')


def create_db():
    create_users_table()
    create_naf_table()
    create_dataset_table()


def create_naf_table():
    naf = pd.read_excel(f"{prepare_dataset.data_path}/table_NAF2-NA.xls", header=[1])
    naf = prepare_dataset.prepare_naf_df(naf)
    naf = prepare_dataset.rename_cols(naf)
    dtypes_dict = prepare_dataset.get_dataset_dtype_dict(naf)
    naf.to_sql('naf', engine, dtype=dtypes_dict)
    add_pk('naf', 'code_ape')

def create_users_table():
    engine.execute(f"""CREATE TABLE IF NOT EXISTS users
        (userid SERIAL PRIMARY KEY,
        username VARCHAR,
        password VARCHAR);
        """)

def drop_table(table_name):
    engine.execute(f"DROP TABLE IF EXISTS {table_name};")
   
def reset_db():
    clear_db()
    create_db()

if __name__ == '__main__':
    engine = sqlalchemy.create_engine(settings.DATABASE_URI, echo=True)
    reset_db()



