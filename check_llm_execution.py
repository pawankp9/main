from llm_client.llm_client import LLMClient
from configs.llm_creds import loadOpeanAICreds
import sys
import warnings
warnings.filterwarnings("ignore")

loadOpeanAICreds()

###########################################################################################
prompt = '''Answer the question precisely, based on your knowledge.
        Here is the question: {question}'''

# question = 'What is the capital of India?'


while True:
        user_input = input('How can I help you today: ')
        if user_input != 'exit':
                chain = LLMClient().execute_llm(prompt)
                llmResponse = chain.invoke({"question": user_input})
                print(f"llmResponse: {llmResponse.content}")
        else:
                print("Hope I was able to help you, Thank You!!")
                sys.exit()
###########################################################################################            
        
