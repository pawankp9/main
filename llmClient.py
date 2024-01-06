from langchain.chains import LLMChain
import openai
import os
from dotenv import load_dotenv

from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
import toml

class LLMClient:
    def __init__(self):
        # Initializing the OpenAI Varibales
        # read local .env file
        # load_dotenv()

        # openai.api_key = os.environ["OPENAI_API_KEY"]
        # openai.api_base = os.environ["OPENAI_API_BASE"]

        config = toml.load("app_config.toml")

        openai.api_key = config["OpenAICreds"]["OPENAI_API_KEY"]
        openai.api_base = config["OpenAICreds"]["OPENAI_API_BASE"]

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

        chat = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
        chain = chat_prompt | chat
        
        return chain