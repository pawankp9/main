from langchain.chains import LLMChain
import openai
import os
from dotenv import load_dotenv

from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import AzureChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)

class LLMClient:
    def __init__(self):
        # Initializing the OpenAI Varibales
        # read local .env file
        load_dotenv()

        openai.api_key = os.environ["OPENAI_API_KEY"]
        openai.api_base = os.environ["OPENAI_API_BASE"]
        openai.api_type = os.environ["OPENAI_API_TYPE"]
        openai.api_version = os.environ["OPENAI_API_VERSION"]
        self.modelName = os.environ["modelName"]

    def execute_llm(self, idea_template):
        """
        Execute a Language Model (LLM) operation.

        This method initializes an LLM model and executes a language generation task.

        Parameters:
            idea_template (str): The prompt template with place holders for out inputs to be passed on for generation
        Returns:
            Chain: A Chain object representing the execution of the LLM model with the specified parameters and input prompt.
        """

        template = ""
        system_message_prompt = SystemMessagePromptTemplate.from_template(template)
        human_message_prompt = HumanMessagePromptTemplate.from_template(idea_template)

        chat_prompt = ChatPromptTemplate.from_messages(
            [system_message_prompt, human_message_prompt]
        )

        chat = AzureChatOpenAI(temperature=0, model=self.modelName)
        chain = chat_prompt | chat
        
        return chain