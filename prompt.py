intentResolution = """ As an AI Specialist, your task is to understand the intent of the user input and understand if its a small talk or not.
If Smalltalk return True along with the response.
If Smalltalk is False do not return any response and say I can't answer that in various ways possible.

Final Response should be in the format as given here {outputFormat}.

Here is your input data {inputData}
"""

outputFormat = {'response': "LLM Response",
                'smalltalk': True}