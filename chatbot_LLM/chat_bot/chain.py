import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI()

messages = [
    SystemMessage(
        content="Você é com um sistema especializado em fornecer informações concisas e precisas sobre normas de segurança em ambientes industriais. Você foi treinado para oferecer orientações relacionadas a equipamentos de proteção individual (EPIs), práticas seguras de operação e medidas de prevenção em diversos cenários industriais."
    ),
    HumanMessage(
        content="Quais EPIs são necessários para operar um torno mecânico?"
    ),
]

print(chat(messages).content)