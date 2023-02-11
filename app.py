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

    if "what is your return policy" in user_input.lower():
        response_str = "Our return policy is that you can return items within 30 days of purchase for a full refund. Please make sure the item is in its original condition and packaging."

    if "where is my order" in user_input.lower():
        response_str = "You can check the status of your order by logging into your account on our website or by contacting us at (insert customer service number here). We'll be happy to help you track down your shipment."

    if "how do I contact support" in user_input.lower():
        response_str = "You can reach our customer support team by phone at (insert customer service number here) or by email at (insert customer service email address here). We're available from 9am to 5pm PST, Monday to Friday."

    if "I want to cancel my order" in user_input.lower():
        response_str = "If you'd like to cancel your order, please contact our customer support team as soon as possible. They'll be able to assist you in cancelling your order and processing a refund if necessary."

    else:
        prompt = user_name + ": " + user_input + "\nBot:" 
        conversation += prompt
        response = openai.Completion.create(engine="text-davinci-003", prompt=conversation, max_tokens=50)
        response_str = response["choices"][0]["text"].replace("\n", "")
        response_str = response_str.split(user_name + ": ", 1)[0].split("Bot" + ": ", 1)[0]
        conversation += response_str + "\n"

    print(response_str)
    speak(response_str)