from dotenv import load_dotenv
import os
import json
import openai

from prompt import *
from llmClient import LLMClient
import pandas as pd
import toml


# Load environment variables
# load_dotenv()

# openai.api_key = os.environ.get("OPENAI_API_KEY")
# openai.api_base = os.environ.get("OPENAI_API_BASE")
# modelname = os.environ.get("modelName")

config = toml.load("app_config.toml")

openai.api_key = config["OpenAICreds"]["OPENAI_API_KEY"]
openai.api_base = config["OpenAICreds"]["OPENAI_API_BASE"]
modelname = config["PARAMS"]["modelName"]
print(f"openai.api_key: {openai.api_key}")
print(f"openai.api_base: {openai.api_base}")
print(f"ModelName: {modelname}")

# language = 'spanish'


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
        return dataFrameEnglish

    except Exception as e:
        print(f"[ERROR]: {e}")
        print(f"[FAILURE]: Unable to Generate English Version.")
        dataFrameEnglish = []
        return dataFrameEnglish

    

