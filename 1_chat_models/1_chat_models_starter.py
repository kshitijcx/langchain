#python -m venv .venv
#.venv\Scripts\activate
#pip install python-dotenv
# from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# llm = ChatOpenAI(model="gpt-3.5-turbo") #ChatOpenAI auto imports key from global env

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
result = llm.invoke("what is the square root of 49")
print(result.content)