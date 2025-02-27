import speech_recognition as sr


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


recognize_speech()
