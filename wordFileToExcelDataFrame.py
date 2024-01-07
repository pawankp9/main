from dotenv import load_dotenv
import os
import json
import openai

from prompt import *
from llmClient import LLMClient
import pandas as pd
import streamlit as st


# Load environment variables
load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")
openai.api_base = os.environ.get("OPENAI_API_BASE")
openai.api_type = os.environ["OPENAI_API_TYPE"]
openai.api_version = os.environ["OPENAI_API_VERSION"]
modelname = os.environ.get("modelName")

def genWordContentToDataframe(wordContent, file_name_without_extension):

    try:
        print("[INFO]: Generating the English version table ...")
        chain = LLMClient().execute_llm(wordToExcelPrompt)
        llmResponse = chain.invoke({"data": wordContent})
        # st.write(f"\nSTEP1: LLMRESPONSE: {llmResponse}")
        # print(f"\nSTEP1: LLMRESPONSE: {llmResponse}")


        llmResponse = llmResponse.content
        llmResponseJSON = json.loads(llmResponse)
        # st.write(f"\nSTEP2: llmResponseJSON: {llmResponseJSON}")
        # print(f"\nSTEP2: llmResponseJSON: {llmResponseJSON}")

        # Create DataFrame
        dataFrameEnglish = pd.DataFrame(llmResponseJSON)
        # st.write(f"\nSTEP3: dataFrameEnglish: {dataFrameEnglish}")
        # print(f"\nSTEP3: dataFrameEnglish: {dataFrameEnglish}")

        # Save DataFrame to Excel
        # dataFrameEnglish.to_csv(file_name_without_extension + "_English.csv", index=False)
        print(f"[SUCCESS]: English Version Generated and saved.")
        return llmResponseJSON

    except Exception as e:
        print(f"[ERROR]: {e}")
        dataFrameEnglish = pd.DataFrame([])
        return dataFrameEnglish

