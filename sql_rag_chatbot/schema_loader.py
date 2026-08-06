# Extract database metadata and turn it into RAG-friendly documents.

from sqlalchemy import create_engine, inspect
from sql_rag_chatbot import config

# Extract schema
def extract_schema():
    connection_string = config.CONNECTION_STRING    
    engine = create_engine(connection_string)
    inspector=inspect(engine)

    schema={}

    for table in inspector.get_table_names():
        if table.lower() == "sysdiagrams":
            continue #exclude sysdiagrams, since it's a SQL Server system table and not part of your business schema.
        columns=inspector.get_columns(table)
        schema[table]=[col['name'] for col in columns]   

    return schema

