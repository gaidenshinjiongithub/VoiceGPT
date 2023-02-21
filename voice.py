import requests
import playsound
import os

def speak(text = None):
    url = "https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    voice_id = "EXAVITQu4vr4xnSDxMaL" #voice id, you can find it in the documentation, i chose bella.
    # api_key = "your api key"

    data = {
    "text": text
    }

    headers = {
        "Content-Type": "application/json",
        "xi-api-key" : api_key
    }

    response = requests.post(url.format(voice_id=voice_id), headers=headers, json=data)

    if response.status_code == 200:

        with open('p.mp3', 'wb') as f:
            f.write(response.content)

        playsound.playsound('p.mp3')
        os.remove("p.mp3")

    else:
        print("Request failed with status code:", response.status_code)