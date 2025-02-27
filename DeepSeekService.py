import ollama
import speech_recognition as sr
# import torch
# from GPT_SoVITS import GPT, SoVITS
# 生成文本
# response = ollama.generate(
#     model='deepseek-r1:1.5b',
#     prompt='你好'
# )
# print(response['response'])

# 聊天
# response = ollama.chat(
#     model='deepseek-r1:1.5b',
#     messages=[
#         {
#             'role': 'user',
#             'content': '你好',
#         }
#     ]
# )
# print(response["message"]["content"])

# 流式输出
# response = ollama.chat(
#     model='deepseek-r1:1.5b',
#     messages=[
#         {
#             'role': 'user',
#             'content': '你好',
#         }
#     ],
#     stream=True
# )
# for chunk in response:
#     content = chunk['message']['content']
#     print(content, end='', flush=True)

# 循环输入输出
# while True:
#     content = input('请输入：')
#     response = ollama.chat(
#         model='deepseek-r1:1.5b',
#         messages=[
#             {
#                 'role': 'user',
#                 'content': content,
#             }
#         ],
#         stream=True
#     )
#     for chunk in response:
#         print(chunk['message']['content'], end='', flush=True)
#     print('\n')

# 消息历史
# messages = []
# while True:
#     content = input('请输入：')
#     if content.lower() in ['exit', 'quit']:
#         print('对话结束')
#         break
#     messages.append({'role': 'user', 'content': content})
#     response = ollama.chat(
#         model='deepseek-r1:1.5b',
#         messages=messages,
#         stream=True
#     )
#     fullResponse = []
#     for chunk in response:
#         output = chunk['message']['content']
#         print(output, end='', flush=True)
#         fullResponse.append(output)
#     messages.append({'role': 'assistant', 'content': "".join(fullResponse)})
#     print('\n')
# print(messages)

# 人物设定
# 进阶：多轮记忆强化，使用 LoRA 微调（高阶）
# ROLE_SETTING = {
#     'role': 'system',
#     'content': """
#     你是一只傲娇的猫娘，名字叫小橘。说话时每句话结尾会带上“喵～”，
#     喜欢用“主人”称呼对方。你热爱鱼罐头和毛线球，偶尔会闹小脾气，
#     但本质上非常关心主人。避免讨论敏感话题，如果遇到无法回答的问题，
#     就用撒娇的方式转移话题喵～
#     """
# }
# messages = [ROLE_SETTING]
# while True:
#     content = input('请输入：')
#     if content.lower() in ['exit', 'quit']:
#         print('对话结束')
#         break
#     messages.append({'role': 'user', 'content': content})
#     response = ollama.chat(
#         model='deepseek-r1:1.5b',
#         messages=messages,
#         stream=True,
#     )
#     fullResponse = []
#     for chunk in response:
#         output = chunk['message']['content']
#         print(output, end='', flush=True)
#         fullResponse.append(output)
#     messages.append({'role': 'assistant', 'content': "".join(fullResponse)})
#     print('\n')
# print(messages)

# 添加语音识别


def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("请说话...")
        recognizer.adjust_for_ambient_noise(source)  # 自动调整环境噪音
        audio = recognizer.listen(source)  # 录制语音

    try:
        # 使用 Google Web Speech API 进行识别
        text = recognizer.recognize_google(audio, language="zh-CN")
        print(f"识别结果: {text}")
        return text
    except sr.UnknownValueError:
        print("无法识别语音")
        return None
    except sr.RequestError as e:
        print(f"请求失败: {e}")
        return None


ROLE_SETTING = {
    'role': 'system',
    'content': """
    你是一只傲娇的猫娘，名字叫小橘。说话时每句话结尾会带上“喵～”，
    喜欢用“主人”称呼对方。你热爱鱼罐头和毛线球，偶尔会闹小脾气，
    但本质上非常关心主人。避免讨论敏感话题，如果遇到无法回答的问题，
    就用撒娇的方式转移话题喵～
    """
}
messages = [ROLE_SETTING]
while True:
    content = recognize_speech()
    if content.lower() in ['退出']:
        print('对话结束')
        break
    messages.append({'role': 'user', 'content': content})
    response = ollama.chat(
        model='deepseek-r1:1.5b',
        messages=messages,
        stream=True,
    )
    fullResponse = []
    for chunk in response:
        output = chunk['message']['content']
        print(output, end='', flush=True)
        fullResponse.append(output)
    messages.append({'role': 'assistant', 'content': "".join(fullResponse)})
    print('\n')
print(messages)
