from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
chat_history = []

systemMsg = SystemMessage(content="You are a helpful AI assistant, answer everything in one line") #optional
chat_history.append(systemMsg)

while True:
    #human message
    query = input("You: ")
    if query.lower() == 'exit':
        break
    chat_history.append(HumanMessage(content=query))

    #llm message
    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response))

    print("AI:",response)

print("--HISTORY--")
print(chat_history)