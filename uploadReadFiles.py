import streamlit as st
from docx import Document

def uploadFiles(uploaded_file):
    # Check if a file is uploaded
    if uploaded_file is not None:
        # Display the uploaded file name
        st.write("Uploaded file:", uploaded_file.name)

        fileContent = ""
        # Read the file and display its content
        if uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            document = Document(uploaded_file)
            paragraphs = [paragraph.text for paragraph in document.paragraphs]
            for paragraph in paragraphs:
                fileContent += paragraph
            return fileContent
        else:
            st.warning("Unsupported file format. Please upload a CSV, Excel, or Word file.")
            return fileContent
    else:
        st.info("Please upload a file.")
        return fileContent