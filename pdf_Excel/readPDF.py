import os
from langchain.document_loaders import PyPDFLoader
from llmClient import LLMClient
from prompts import *

def loadFiles(file):
    """
    Extract text from PDF and TXT files.

    Parameters:
    - files (list): List of file objects (either PDF or TXT).

    Returns:
    - str: Concatenated text extracted from all pages.
    """

    text = ""
    fName = os.path.split(file)[1]

    if fName.lower().endswith(".pdf"):
        print("PDF file detected")

        # [Approach:1:] Process PDF files
        # pdf_reader = PdfReader(file)
        # for page in pdf_reader.pages:
        #     text += page.extract_text()
        
        # [Approach:2:] Process PDF files
        loader = PyPDFLoader(file)
        pages = loader.load_and_split()
        all_page_content = [document.page_content for document in pages]
        for cont in all_page_content:
            text += cont
        return text

    elif fName.lower().endswith(".txt"):
        print("TXT file detected")
        # Process TXT files
        with open(file, 'r', encoding='utf-8') as txt_file:
            text += txt_file.read()
        return text, fName
    else:
        print("No Files found at provided folder path")
        return text, fName

# Provide the path to your PDF file
# pdf_file_path = 'RTMS - Change Management - Assessment Questions.pdf'
# pdf_file_path = 'RTMS - Problem Management - Assessment Questions.pdf'
# pdf_file_path = 'Change Management - Assessment Questions.pdf'
pdf_file_path = 'Problem Management - Assessment Questions.pdf'
pdf_content = loadFiles(pdf_file_path)
# print(pdf_content)


chain = LLMClient().execute_llm(docToTable)
llmResponse = chain.invoke({"QUESTIONAIRE": pdf_content})
print(llmResponse.content)
llmResponse = llmResponse.content



# Find the index where the JSON data starts
data_start_index = llmResponse.find('{')
data_end_index = llmResponse.find('}') + 1
json_data_string = llmResponse[data_start_index:data_end_index]  # Extract the JSON data string
print(f"EXTRACTED RESPONSE: {json_data_string}")

print(f"\n\nDF-INPUT-DATA: {[json_data_string]}")

import json
llmResponseJSON = json.loads(json_data_string)
print(f"\n\nDF-INPUT-DATA-JSON: {llmResponseJSON}")

# Create DataFrame
import pandas as pd
dataFrameEnglish = pd.DataFrame(llmResponseJSON)
print(f"\n\nDataFrameGenerated: {dataFrameEnglish}")

# Save DataFrame to Excel
file_name_without_extension, _ = os.path.splitext(os.path.basename(pdf_file_path))
dataFrameEnglish.to_csv(file_name_without_extension + "_English.csv", index=False)