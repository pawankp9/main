wordToExcelPrompt = """ As an AI model expert, your task is to format the given data into a structured table.
Table will have the below columns.
Questions A  B  C  D  Correct Answers
Data should be aligned appropriately in the above columns.
The final response should be a list  with all the informations neeede to create pandas dataframe with the mentioned columns and its corresponding data.
DO NOT ADD ANYTHING ADDITIONAL APART FROM THE DATA INT HE FINAL RESPONSE.
Here is the {data}
"""
# The final response should be a dataframe with the mentioned columns and its corresponding data.

languageTranslation = """As an AI language expert you are tasked to translate the given table into the mentioned language.
The final response should be a LIST with all the informations required to create pandas dataframe directly with the mentioned columns and its corresponding data.
The language to be translated into is {language}.

Column Name in the dataframe should always be followed as given below without fail:
Questions A  B  C  D  Correct Answers
Questions columns should have the questions.
and the columns A, B, C, D should have the corresponding options and
Correct Answer column should have the correct answer corresponding to the question

Here is the {dataTable} to be translated.
"""


llmResponse = [
    {
        "Questions": "How do you access Yammer in Yammer Web 2020?",
        "A": "Through the Yammer desktop application",
        "B": "Using a company email address and accessing via Office 365",
        "C": "By downloading the Yammer app on a mobile device",
        "D": "Via a direct link in an email",
        "Correct Answers": "b) Using a company email address and accessing via Office 365"
    },
    {
        "Questions": "What can be customized in your Yammer profile?",
        "A": "Your network and group memberships",
        "B": "Interests, expertise, work history, profile picture, and birthday",
        "C": "The layout of the Yammer feed",
        "D": "The design of the Yammer interface",
        "Correct Answers": "b) Interests, expertise, work history, profile picture, and birthday"
    },
    {
        "Questions": "How do you navigate between different versions of Yammer?",
        "A": "By changing settings in the Profile menu",
        "B": "Using a toggle switch between the new and classic versions",
        "C": "By installing different versions of the application",
        "D": "The version cannot be changed",
        "Correct Answers": "b) Using a toggle switch between the new and classic versions"
    },
    {
        "Questions": "What is the purpose of the Yammer inbox?",
        "A": "To organize, read, and reply to messages",
        "B": "To store files and documents",
        "C": "To customize user settings",
        "D": "To manage group memberships",
        "Correct Answers": "a) To organize, read, and reply to messages"
    },
    {
        "Questions": "How do you send a private message in Yammer?",
        "A": "Through the main feed",
        "B": "Using the New Private Message button",
        "C": "By tagging a user in a public post",
        "D": "Via the Files tab",
        "Correct Answers": "b) Using the New Private Message button"
    },
    {
        "Questions": "What feature is used to manage and organize messages in Yammer?",
        "A": "The Communities tab",
        "B": "The Files directory",
        "C": "The inbox management tools",
        "D": "The profile settings",
        "Correct Answers": "c) The inbox management tools"
    },
    {
        "Questions": "How can you reply to messages in Yammer?",
        "A": "By creating a new post in the feed",
        "B": "Using the Comment button beneath a message",
        "C": "Through the Yammer desktop application only",
        "D": "By sending an email",
        "Correct Answers": "b) Using the Comment button beneath a message"
    },
    {
        "Questions": "What is a method for marking messages as read or unread in Yammer?",
        "A": "Through the Office 365 settings",
        "B": "Using a checkmark icon in the inbox",
        "C": "By opening each message individually",
        "D": "This feature is not available in Yammer",
        "Correct Answers": "b) Using a checkmark icon in the inbox"
    },
    {
        "Questions": "How do you update your Yammer profile?",
        "A": "By emailing the Yammer support team",
        "B": "Using the Edit settings link in the Settings panel",
        "C": "Through the Communities tab",
        "D": "Profile updates are not permitted",
        "Correct Answers": "b) Using the Edit settings link in the Settings panel"
    },
    {
        "Questions": "What is the function of the app launcher in Yammer Web 2020?",
        "A": "To close the Yammer application",
        "B": "To navigate to other Office applications",
        "C": "To change language settings",
        "D": "For editing user profiles",
        "Correct Answers": "b) To navigate to other Office applications"
    }
]