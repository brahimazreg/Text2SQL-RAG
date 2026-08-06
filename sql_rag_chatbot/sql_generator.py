from google import genai
from sql_rag_chatbot import config


client = genai.Client(
    api_key=config.GEMINI_API_KEY
)


def generate_sql(question, schema):
    
    prompt = config.PROMPT.format(
    schema=schema,
    query=question
)
    
    response = client.models.generate_content(
        model=config.LLM_MODEL_NAME,
        contents=prompt
    )

    return response.text

