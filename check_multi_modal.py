from langchain_core.messages import HumanMessage
from langchain_community.chat_models import AzureChatOpenAI
model = AzureChatOpenAI(model="gpt4o")
import warnings
warnings.filterwarnings("ignore")
from configs.llm_creds import loadOpeanAICreds

loadOpeanAICreds()

image_url = 'https://c8.alamy.com/comp/CF3FEE/test-match-cricket-in-play-at-lords-cricket-ground-in-london-CF3FEE.jpg'
message = HumanMessage(
    content=[
        {"type": "text", "text": "describe this image, and tell me which 2 countries are playing against each other in this match"},
        {"type": "image_url", "image_url": {"url": image_url}},
    ],
)
response = model.invoke([message])
print(response.content)