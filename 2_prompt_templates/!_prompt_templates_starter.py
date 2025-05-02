from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

template = "Write a {tone} email to {company} expressing interest in the {position}, mentioning {skill} as a key strength. Keep it 4 lines max"

prompt_template = ChatPromptTemplate.from_template(template)

print(prompt_template)

#create a prompt with a list that contains only HumanMessage
prompt = prompt_template.invoke({
    "tone":"energetic",
    "company":"samsung",
    "position":"AI Engineer",
    "skill":"AI"
})

print(prompt)

result = llm.invoke(prompt)
print(result.content) 

messages = [
    ("system","you are a comedian who tells jokes about {topic}"),
    ("human","tell me {joke_count} jokes")
]

#creates a list with SystemMessage and HumanMessage
prompt_template_new = ChatPromptTemplate(messages)
prompt_new =  prompt_template_new.invoke({
    "topic":"mathematics",
    "joke_count":3
})
print(prompt_new)