from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

prompt_template = ChatPromptTemplate([
    ("system","You are expert on {animal}"),("human","Tell me {fact_count} short facts")
])

#create a combined chain using langchain expression language (LCEL)
chain = prompt_template | model | StrOutputParser() #StrOutputParser method extracts content
 
result = chain.invoke({"animal":"cat","fact_count":2}) #the object will be available throughout the chain

print(result)