import openai
import speech_recognition as sr
import os
import playsound 
from gtts import gTTS

openai.api_key = "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"

r = sr.Recognizer()
mic = sr.Microphone(device_index=1)

print(sr.Microphone.list_microphone_names())

conversation = ""
user_name = "Edward"

while True: 
    with mic as source:
        print("\nlistening...")
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)
    print("no longer listening. \n")

    try:
        user_input = r.recognize_google(audio)
    except:
        continue

    prompt = user_name + ": " + user_input + "\nBot:" 

    conversation +=  prompt

    response = openai.Completion.create(engine="text-davinci-003", prompt=conversation, max_tokens=50)
    response_str = response["choices"][0]["text"].replace("\n", "")
    response_str = response_str.split(user_name + ": ", 1)[0].split("Bot" + ": ", 1)[0]

    conversation += response_str + "\n"

    print(response_str)
    # Generate audio using gTTS
    tts = gTTS(text=response_str, lang='en')
    tts.save("tts.mp3")
    # Play the generated audio
    playsound.playsound("tts.mp3")
    os.remove("tts.mp3")
    # os.system("start tts.mp3")