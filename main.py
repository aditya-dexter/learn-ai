import os

from dotenv import load_dotenv
from langchain import hub
from langchain.agents import AgentExecutor
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from langchain.agents.react.agent import create_react_agent
from langchain_tavily import TavilySearch

load_dotenv()

tools = [TavilySearch()]
react_prompt = hub.pull("hwchase17/react")

llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash-001",
        api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0.0
    )

agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=react_prompt
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
chain = agent_executor

def main():
    print("Starting the agent...")

    result = chain.invoke(
        {
            "input": "What is the latest news on the stock market?"
        }
    )
    print(result)

if __name__ == "__main__":
    main()
