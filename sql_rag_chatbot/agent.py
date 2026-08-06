
# The agent is the component that connects all the modules together.
# It does not do the work itself; it coordinates the workflow.( pipeline)

from sql_rag_chatbot.retriever import retrieve
from sql_rag_chatbot.sql_generator import generate_sql
from sql_rag_chatbot.validator import validate_sql
from sql_rag_chatbot.connect_database import execute_query


def answer_question(question):

    schema = retrieve(question)

    sql = generate_sql(
        question,
        schema
    )

    sql = validate_sql(sql)

    columns ,result = execute_query(sql)

    return columns , result