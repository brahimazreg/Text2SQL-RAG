from sql_rag_chatbot.schema_loader import extract_schema


def test_schema():
    schema = extract_schema()

    for table, columns in schema.items():
           print(f"\nTable: {table}")
           print(f"Columns: {columns}")

if __name__ == "__main__":
    test_schema()