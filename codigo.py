from dotenv import load_dotenv
import os 
from langchain_core.messages import SystemMessage,HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()
chave_api = os.getenv("OPENAI_API_KEY")

mensagens = [
    SystemMessage("traduza o texto a seguir para inglês "),
    HumanMessage("se inscrevam no canal ")
]

modelo = ChatOpenAI(model="gpt-3.5-turbo")
parser =StrOutputParser()
chain = modelo | parser 


templet_mensagen = ChatPromptTemplate.from_messages([
    ("system","traduza o texto a seguir {idioma}"),
    ("user", "{texto}"),
])

#print(templet_mensagen.invoke({"idioma": "frances", "texto" : "de like no video"}))

chain = templet_mensagen | modelo | parser  

#texto = chain.invoke({"idioma": "frances","texto": "de like no video "})

#print(texto)