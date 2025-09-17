import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama

load_dotenv()


def main():
    print("Hello from learn-ai!")
    print(os.getenv("GOOGLE_API_KEY"))

    information = """
    Aditya is a helpful assistant that can answer questions and help with tasks. 
    He is a student of Computer Science and Engineering at the University of Delhi.
    He is a good student and he is a good person.
    """

    summary_template = """
        {information}
        Please summarize the information in a one sentence.
    """

    prompt = PromptTemplate(
        template=summary_template,
        input_variables=["information"]
    )

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash-001",
        api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0.0
    )

    llmOllama = ChatOllama(
        model="gemma3:latest",
        temperature=0.0
    )

    chain = prompt | llmOllama

    result = chain.invoke({"information": information})
    print(result.content)

if __name__ == "__main__":
    main()
