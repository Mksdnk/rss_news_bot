from azure.ai.inference.aio import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.inference.models import SystemMessage, UserMessage
from bot.config_reader import config

endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1"
token = config.CHAT_GPT_API_KEY.get_secret_value()

client = ChatCompletionsClient(endpoint, AzureKeyCredential(token))

async def get_chat_gpt_response(prompt: str):
    messages = [SystemMessage(content="You are a helpful assistant."), UserMessage(content=prompt)]
    response = await client.complete(messages=messages, model=model, temperature=0.8, top_p=1.0)
    return response.choices[0].message.content