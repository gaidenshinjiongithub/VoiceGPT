import openai
import pyttsx3
import speech_recognition as sr


openai.api_key = "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"

engine = pyttsx3.init()

r = sr.Recognizer()
mic = sr.Microphone(device_index=1)

print(sr.Microphone.list_microphone_names())

conversation = ""
user_name = "daron"

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

    engine.say(response_str)
    engine.runAndWait()