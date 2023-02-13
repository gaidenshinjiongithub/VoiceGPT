import openai
import speech_recognition as sr
import os
import playsound
from thefuzz import fuzz
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


    if fuzz.token_set_ratio(user_input.lower(), "return policy") >= 60 or fuzz.token_set_ratio(user_input.lower(), "repeat") >= 60:
        response_str = "Our return policy is that you can return items within 30 days of purchase for a full refund."
        
    elif fuzz.token_set_ratio(user_input.lower(), "order status") >= 60 or fuzz.token_set_ratio(user_input.lower(), "repeat") >= 60:
        response_str = "You can check the status of your order by logging into your account on our website"

    elif fuzz.token_set_ratio(user_input.lower(), "customer support") >= 60 or fuzz.token_set_ratio(user_input.lower(), "repeat") >= 60:
        response_str = "You can reach our customer support team by phone"

    elif fuzz.token_set_ratio(user_input.lower(), "cancel order") >= 60 or fuzz.token_set_ratio(user_input.lower(), "repeat") >= 60:
        response_str = "If you'd like to cancel your order, please contact customer support"

    elif fuzz.token_set_ratio(user_input.lower(), "shipping information") >= 60 or fuzz.token_set_ratio(user_input.lower(), "repeat") >= 60:
        response_str = "You can find our shipping information, including transit times and delivery dates, on our website"
   

    else:
        prompt = user_name + ": " + user_input + "\nBot:" 
        conversation += prompt
        response = openai.Completion.create(engine="text-davinci-003", prompt=conversation, max_tokens=50)
        response_str = response["choices"][0]["text"].replace("\n", "")
        response_str = response_str.split(user_name + ": ", 1)[0].split("Bot" + ": ", 1)[0]
        conversation += response_str + "\n"

    print(response_str)
    speak(response_str)