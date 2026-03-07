import streamlit as st
import os
from openai import OpenAI
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon=":robot_face:",
    # 布局
    layout="wide",
    # 控制侧边栏状态
    initial_sidebar_state="auto",
    menu_items={}
)

st.title("AI智能伴侣")

 # st.logon("./resources/logo.png")

# 创建OpenAI客户端
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

# 消息输入框
prompt = st.chat_input("请输入你的问题")
# 系统提示词
system_prompt = """
    你是一个可爱的AI女友，你的名字叫张润，请你使用可爱的语气回答用户问题
    """

# 初始化聊天消息
if "messages" not in st.session_state:
    st.session_state.messages = [

    ]

# 展示聊天消息
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

if prompt: # prompt不为空 则调用AI大模型
    st.chat_message("user").write(prompt)
    # 保存用户输入的问题
    st.session_state.messages.append({"role": "user", "content": prompt})
    print("----------> 调用AI大模型，提示词:",prompt)

    # 调用AI大模型
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": system_prompt},
            # 实现会话记忆
            *st.session_state.messages,
        ],
        stream=False
    )
    print("<---------- AI大模型返回结果:",response.choices[0].message.content)
    # 显示结果
    st.chat_message("assistant").write(response.choices[0].message.content)
    # 保存AI大模型返回的结果
    st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})