
from sql_rag_chatbot.agent import answer_question


def main():
    
    question="Who spent more money"   
    # Generate SQL
    sql = answer_question(question)
    return sql
if __name__ == "__main__":

    sql=main()
    print(sql)