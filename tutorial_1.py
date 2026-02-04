from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from config import Config

print("Using OpenAI API Key:", Config.OPENAI_API_KEY)
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=Config.OPENAI_API_KEY)

response = llm([
    HumanMessage(content="Explain closures in JavaScript in 2 lines")
])

print(response.content)
