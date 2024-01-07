from llmClient import LLMClient
from prompt import intentResolution, outputFormat
import sys
from dotenv import load_dotenv
import openai
import os

def loadOpeanAICreds():
    load_dotenv()
    azure = True
    try:
        openai.api_key = os.environ["OPENAI_API_KEY"]
        openai.api_base = os.environ["OPENAI_API_BASE"]
        openai.api_type= os.environ["OPENAI_API_TYPE"]
        openai.api_version= os.environ["OPENAI_API_VERSION"]
    except Exception as e:
        print("Value Not found")
        azure = False

    if azure is True:
        print(f"---------- Working with AZURE ----------")
        print(f"KEY: {openai.api_key}")
        print(f"BASE: {openai.api_base}")
        print(f"TYPE: {openai.api_type}")
        print(f"VERSION: {openai.api_version}")  

    else:
        print(f"---------- Working with OPENAI ----------")
        print(f"KEY: {openai.api_key}")
        print(f"BASE: {openai.api_base}")
        print(f"TYPE: {openai.api_type}")
        print(f"VERSION: {openai.api_version}")

loadOpeanAICreds()        
sys.exit()


while True:
    userQuery = input("Hey! How can I help you today?: ")
    if userQuery != 'exit':
        chain = LLMClient().execute_llm(intentResolution)
        llmResponse = chain.invoke({"outputFormat": outputFormat, "inputData": userQuery})
        print(f"llmResponse: {llmResponse.content}")
    else:
        print(f"Hope I was Helpful to you, Thanks, Bye!!")
        sys.exit()