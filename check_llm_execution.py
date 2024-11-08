from llm_client.llm_client import LLMClient
from configs.llm_creds import loadOpeanAICreds

loadOpeanAICreds()

prompt = '''Answer the question precisely, only based on your knowledge.
        Here is the question: {question}'''

question = 'What is the capital of India?'

chain = LLMClient().execute_llm(prompt)
llmResponse = chain.invoke({"question": question})
print(f"llmResponse: {llmResponse.content}")

