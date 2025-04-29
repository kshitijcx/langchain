from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
messages = [
    SystemMessage("You are an expert in Mathematics"),
    HumanMessage("Give a short tip on how to score good in Mathematics exams"),
    # AIMessage("")
]

result = llm.invoke(messages)
print(result.content)