from dotenv import load_dotenv
import json
from prompt import *
from llmClient import LLMClient
import pandas as pd
import streamlit as st

def languageTranslator(dataFrameEnglish, language, file_name_without_extension):

    try:
        print(f"\n\n[INFO]: Generating the {language} version table ...")
        chain = LLMClient().execute_llm(languageTranslation)
        llmResponse = chain.invoke({"dataTable": dataFrameEnglish, "language": language, "wordToExcelPrompt": wordToExcelPrompt})

        llmResponse = llmResponse.content
        st.write(f"\nSTEP1: LLMRESPONSE: {llmResponse}")

        # data_start_index = llmResponse.find('[')  # Find the index where the JSON data starts
        # json_data_string = llmResponse[data_start_index:]  # Extract the JSON data string
        # st.write(f"\nSTEP2: json_data_string: {json_data_string}")

        # Convert the JSON data string to a list of dictionaries
        llmResponseJSON = json.loads(llmResponse)
        st.write(f"\nSTEP3: llmResponseJSON: {llmResponseJSON}")

        # Create DataFrame
        dataFrameTranslated = pd.DataFrame(llmResponseJSON)
        st.write(f"\nSTEP4: llmResponseJSON: {dataFrameTranslated}")

        # Save DataFrame to Excel
        # dataFrameTranslated.to_csv(file_name_without_extension + "_" + language + ".csv", index=False)
        print(f"[SUCCESS]: {language} Version Generated and saved.")
        return dataFrameTranslated
    
    except Exception as e:
        print(f"[ERROR]: {e}")
        return pd.DataFrame([])
