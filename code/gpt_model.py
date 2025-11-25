from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

gpt_model = ChatOpenAI(model="gpt-4o-mini")
