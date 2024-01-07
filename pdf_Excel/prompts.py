docToTable = """As an AI model expert, your task is to format the given QUESTIONAIRE into a structured table.
Put the QUESTIONAIRE provided into a table with columns as below:
Questions, A, B, C, D, E, F.
The questions might vary, few have 2 options few have 3 and few have even 4 or 5, need to adjust dynamically and create the table.

The Final response should always be a pandas dataframe with all the columns information and the corresponding data.
{QUESTIONAIRE} 
"""
