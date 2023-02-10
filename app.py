import openai
import speech_recognition as sr
import os
import playsound
from voice import speak

openai.api_key = "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"

r = sr.Recognizer()
mic = sr.Microphone(device_index=2)

for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

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

    if "do something" in user_input.lower():
        response_str = "Playing a sound."
    else:
        prompt = user_name + ": " + user_input + "\nBot:" 
        conversation += prompt
        response = openai.Completion.create(engine="text-davinci-003", prompt=conversation, max_tokens=50)
        response_str = response["choices"][0]["text"].replace("\n", "")
        response_str = response_str.split(user_name + ": ", 1)[0].split("Bot" + ": ", 1)[0]
        conversation += response_str + "\n"

    print(response_str)
    speak(response_str)