from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

#loading the api key
load_dotenv()

#llm
llm = ChatGroq(groq_api_key = os.getenv("GROQ_API_KEy"), model_name = 'llama-3.3-70b-versatile')


if __name__ == '__main__':
    res = llm.invoke("Hello, write a poem on yourself")
    print(res.content)