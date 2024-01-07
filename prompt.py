wordToExcelPrompt = """ As an AI model expert, your task is to format the given data into a structured table.
Table should have the below columns.
Questions A  B  C  D  Correct Answers
Data should be aligned appropriately in the above columns, and column names should be the same as above.
The final response should be a list  with all the informations neeede to create pandas dataframe with the mentioned columns and its corresponding data.
DO NOT ADD ANYTHING ADDITIONAL APART FROM THE DATA INT HE FINAL RESPONSE.
Here is the {data}
"""

# The final response should be a LIST with all the informations required to create pandas dataframe directly with the mentioned columns and its corresponding data.
languageTranslation = """As an AI language expert you are tasked to translate the given table into the mentioned language.
The language to be translated into is {language}.

Column Name in the dataframe should always be followed as given below without fail:
Questions A  B  C  D  Correct Answers
Questions columns should have the questions.
and the columns A, B, C, D should have the corresponding options and
Correct Answer column should have the correct answer corresponding to the question

Here is the {dataTable} to be translated.
"""

# languageTranslation = """As an AI language expert you are a language expert and are expert in multiple languages across the glob.
# Your task is to translate this table {dataTable} into {language} language.
# Final Response should follow the below instructions to generate the response.
# {wordToExcelPrompt}
# """


# languageTranslation = """As an AI Expert you are a Multi language Specialist from languages across the world.
# Your task is to translate the given data into {language} language.
# Always Keep the final response format as given in the input format without fail.

# Here is your data to work with {dataTable}
# """


docToTable = """As an AI model expert, your task is to format the given QUESTIONAIRE into a structured table.
Put the QUESTIONAIRE provided into a table with columns as below:
Questions, A, B, C, D, E, F.
The questions might vary, few have 2 options few have 3 and few have even 4 or 5, need to adjust dynamically and create the table.

The Final response should always be a pandas dataframe with all the columns information and the corresponding data.
{QUESTIONAIRE} 
"""
