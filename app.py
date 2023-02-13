import openai
import speech_recognition as sr
import playsound
import gradio as gr
from thefuzz import fuzz
from voice import speak

openai.api_key = "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"

r = sr.Recognizer()
mic = sr.Microphone(device_index=2)

def main(inputs):
    conversation = ""
    user_name = "Edward"

    user_input = inputs[0]

    if fuzz.token_set_ratio(user_input.lower(), "return policy") >= 60 or fuzz.token_set_ratio(user_input.lower(), "repeat") >= 60:
        response_str = "Our return policy is that you can return items within 30 days of purchase for a full refund."

    elif fuzz.token_set_ratio(user_input.lower(), "order status") >= 60 or fuzz.token_set_ratio(user_input.lower(), "repeat") >= 60:
        response_str = "You can check the status of your order by logging into your account on our website."

    else:
        prompt = user_name + ": " + user_input + "\nBot:" 
        conversation += prompt
        response = openai.Completion.create(engine="text-davinci-003", prompt=conversation, max_tokens=50)
        response_str = response["choices"][0]["text"].replace("\n", "")
        response_str = response_str.split(user_name + ": ", 1)[0].split("Bot" + ": ", 1)[0]
        conversation += response_str + "\n"

    return speak(response_str)

app = gr.Interface(main, ["text"], "audio", examples=[("What's your return policy?",)])
app.launch()
