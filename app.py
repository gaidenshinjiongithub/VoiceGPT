import openai
import gradio as gr
from voice import speak

# openai.api_key = "YOUR_API_KEY"

def main(inputs):
    conversation = ""
    user_name = "user"

    user_input = inputs[0]
    
    # Prompt to be sent to OpenAI API
    prompt = user_name + ": " + user_input + "\nBot:" 

    # Send prompt to OpenAI API
    response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=50)
    response_str = response["choices"][0]["text"].replace("\n", "")
    
    # Extract only the bot's response from the full response string
    response_str = response_str.split(user_name + ": ", 1)[0].split("Bot" + ": ", 1)[0]

    return speak(response_str)

with gr.Blocks() as demo:

    chatbox = gr.Textbox(label="enter message: ")
    send_btn = gr.Button(value="Send")

    output = gr.Audio(label="Chat Output")

    send_btn.click(main, inputs=chatbox, outputs=output)

demo.launch()
