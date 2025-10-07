import os
from pymongo import MongoClient

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.agents import initialize_agent, AgentType
from langchain_mongodb.agent_toolkit import MongoDBDatabase, MongoDBDatabaseToolkit

load_dotenv()


llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.6)

conn_string=os.getenv("MONGO_CONNECTION_STRING")

db=MongoDBDatabase.from_connection_string(conn_string)

toolkit=MongoDBDatabaseToolkit(db=db, llm=llm)


all_tool=toolkit.get_tools()

tools=[t for t in all_tool if t.name in ('mongodb_query', 'mongodb_schema', 'mongodb_list_collections', 'mongodb_query_checker')]

agent=initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

prompt = """
Find products under $50 with tag 'smart'. 
Return name, price, and stock.
Use aggregate() with valid Python dictionary syntax (double quotes, keys quoted, '$' prefixed).
If none found, say 'No products found'.
"""
print(agent.run(prompt))
