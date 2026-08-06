from sql_rag_chatbot.connect_database import connect_sqldb 

# Test Database Connection

db=connect_sqldb()
print("Available Tables:")
print(db.get_usable_table_names())

print("\n:top 5 customers")
(
        print(db.run(
            "select top 5 * from Customer"
        ))
)
import pyodbc
from sql_rag_chatbot import config

print("=== DEBUG TEST ===")

print(pyodbc.drivers())

print(config.CONNECTION_STRING)