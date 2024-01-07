import streamlit as st
import pandas as pd
from readWordFile import read_word_file
from wordFileToExcelDataFrame import genWordContentToDataframe
from EnglishToLanguageTranslator import languageTranslator
from uploadReadFiles import uploadFiles

# Function to read word file
@st.cache(allow_output_mutation=True)
def read_word_content(file_path):
    word_content, file_name_without_extension = read_word_file(file_path)
    return word_content, file_name_without_extension

# Function to generate Excel and return DataFrame
@st.cache(allow_output_mutation=True)
def generate_excel_df(word_content, file_name_without_extension):
    df_english = genWordContentToDataframe(word_content, file_name_without_extension)
    return df_english

# Function to translate DataFrame to another language
@st.cache(allow_output_mutation=True)
def translate_to_language(df, language, file_name_without_extension):
    df_translated = languageTranslator(df, language, file_name_without_extension)
    return df_translated

def lanSelection():
    st.header("Languages Supported")
    options = ["None", "Spanish", "French", "German", "Chinese"]
    
    # Display the selectbox
    selected_option = st.selectbox("Choose the language you want to continue with:", options)
    
    # Check if the user has made a selection
    if selected_option != "None":
        # Return the selected option only if it's not the default value
        return selected_option
    else:
        # If the user selected the default value, provide a message or handle it as needed
        st.warning("Please select a valid language to proceed.")
        # You may choose to return a default value or None in this case
        return None

# Streamlit app
st.title("Language Conversion App")

# File upload
uploaded_file = st.file_uploader("Choose your Word Files and Press OK", type=['docx'], accept_multiple_files=False)

if uploaded_file is not None:
    # uploaded_file = "uploadedData/" + str(uploaded_file.name)
    word_content = uploadFiles(uploaded_file)
    file_name_without_extension = "DummmyName"

    # Read Word content
    # with st.spinner(f"Processing your word file ..."):
    #     word_content, file_name_without_extension = read_word_content(uploaded_file)

    # Display original content
    with st.spinner(f"LOADING and EXTRACTING content from the file: {file_name_without_extension} ..."):
        # Generate Excel DataFrame
        df_english = generate_excel_df(word_content, file_name_without_extension)

        # Display DataFrame
        st.subheader("Excel DataFrame (English):")
        st.dataframe(df_english)

        selected_language = lanSelection()  

        if selected_language is not None:
            st.write(f"You selected: {selected_language.lower()}")

            # Translate to selected language
            with st.spinner(f"Processing English to {selected_language} ..."):
                df_translated = translate_to_language(df_english, selected_language, file_name_without_extension)

                # Display translated content
                st.subheader(f"Translated Content into ({selected_language}):")
                st.dataframe(df_translated)
