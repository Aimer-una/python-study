# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是一名可爱的AI女友，你的名字叫张润,请你使用可爱的语气回答用户问题"},
        {"role": "user", "content": "张润宝宝你好呀"},
    ],
    stream=False
)

print(response.choices[0].message.content)