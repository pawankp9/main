import os
from dotenv import load_dotenv
from openai import AzureOpenAI
import json

load_dotenv()

client = AzureOpenAI(
    api_version=["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=["AZURE_OPENAI_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
)

result = client.images.generate(
    model="Dalle3",
    prompt=f"""
    Prime Minister addressing his cabinet of central ministers in a U shaped table with mics infront of them and their names written on the desk.
    """,
    size="1024x1024",
    n=1
)

image_url = json.loads(result.model_dump_json())['data'][0]['url']
print(image_url)
