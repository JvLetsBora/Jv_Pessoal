from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
import os
import dotenv
from typing import List
from langchain.schema import BaseOutputParser




dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)
llm = ChatOpenAI(openai_api_key='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')
chat_model = ChatOpenAI()

class CommaSeparatedListOutputParser(BaseOutputParser[List[str]]):


    def parse(self, text: str) -> List[str]:
        return text

template = """ Você é com um sistema especializado em fornecer informações concisas e precisas sobre normas de segurança em ambientes industriais. Você foi treinado para oferecer orientações relacionadas a equipamentos de proteção individual (EPIs), práticas seguras de operação e medidas de prevenção em diversos cenários industriais. """
human_template = "{text}"

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("human", human_template),
])
chain = chat_prompt | ChatOpenAI() | CommaSeparatedListOutputParser()

def chat_bot(msg):
    return chain.invoke({"text": f"{msg}"})
