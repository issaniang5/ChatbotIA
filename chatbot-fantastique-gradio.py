import openai
import gradio as gr
import yaml

# Lecture d'un fichier yml privé
with open("pass.yml") as f:
    content = f.read()
    
# Importer le nom d'utilisateur et le mot de passe depuis credentials.yml
my_credentials = yaml.load(content, Loader=yaml.FullLoader)

openai.api_key = my_credentials["api"]

messages = [
    {"role": "system", "content": "You are a helpful and kind AI Assistant."},
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

inputs = gr.inputs.Textbox(lines=7, label="Chat with AI")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="AI Chatbot",
             description="Ask anything you want",
             theme="compact").launch(share=True)
