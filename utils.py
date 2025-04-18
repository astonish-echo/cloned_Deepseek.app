from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI

#import os
from langchain.memory import ConversationBufferMemory


def get_chat_response(prompt, memory, openai_api_key):
    model = ChatOpenAI(model="deepseek-chat", openai_api_key=openai_api_key,openai_api_base="https://api.deepseek.com")
    chain = ConversationChain(llm=model, memory=memory)

    response = chain.invoke({"input": prompt})
    return response["response"]


memory = ConversationBufferMemory(return_messages=True)
#print(get_chat_response("牛顿提出过哪些知名的定律？", memory, os.getenv("DEEPSEEK_API_KEY")))
#print(get_chat_response("你好？", memory, os.getenv("DEEPSEEK_API_KEY")))
