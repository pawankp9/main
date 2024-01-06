from dotenv import load_dotenv
import os
import json
import openai

from prompt import *
from llmClient import LLMClient
import pandas as pd


# Load environment variables
load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")
openai.api_base = os.environ.get("OPENAI_API_BASE")
modelname = os.environ.get("modelName")

language = 'spanish'



def genWordContentToDataframe(wordContent, file_name_without_extension):

    try:
        print("[INFO]: Generating the English version table ...")
        chain = LLMClient().execute_llm(wordToExcelPrompt)
        llmResponse = chain.invoke({"data": wordContent})

        llmResponse = llmResponse.content
        llmResponseJSON = json.loads(llmResponse)

        # Create DataFrame
        dataFrameEnglish = pd.DataFrame(llmResponseJSON)

        # Save DataFrame to Excel
        # dataFrameEnglish.to_csv(file_name_without_extension + "_English.csv", index=False)
        print(f"[SUCCESS]: English Version Generated and saved.")

    except Exception as e:
        print(f"[ERROR]: {e}")

    return dataFrameEnglish

