from sqlalchemy import create_engine
from langchain_community.utilities import SQLDatabase
from sql_rag_chatbot import config

from sqlalchemy import text

# SQL Server Connection
    
def connect_sqldb():
     
    connection_string = config.CONNECTION_STRING
    engine = create_engine(connection_string)
    db = SQLDatabase(engine) 
    print("Drivers:")  

    print("Connection string:")
    print(config.CONNECTION_STRING)
  
    return db

def execute_query(sql):

    db = connect_sqldb()

    with db._engine.connect() as connection:
        result = connection.execute(text(sql))

        columns = result.keys()
        rows = result.fetchall()

    return columns, rows

""" def get_connection():
    print("=== DEBUG DATABASE ===")

    print("Drivers:")
    print(pyodbc.drivers())

    print("Connection string:")
    print(config.CONNECTION_STRING)
    connection = pyodbc.connect(
        config.CONNECTION_STRING
    )

    return connection """


