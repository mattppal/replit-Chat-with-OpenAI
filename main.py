import os

import gradio as gr
import openai

openai.api_key = os.environ['OPENAI_API_KEY']


def chat_with_replit(message, history):

  messages = []
  for h in history:
    u = str(h[0])
    s = str(h[1])

    messages.append({"role": 'user', "content": u})
    messages.append({"role": 'assistant', "content": s})

  messages = messages + [
      {
          "role": "user",
          "content": str(message),
      },
  ]

  response = openai.chat.completions.create(model="gpt-4o", messages=messages)

  return response.choices[0].message.content


with gr.Blocks(fill_height=True) as demo:
  gr.ChatInterface(chat_with_replit,
                   fill_height=True,
                   examples=[
                       "What is the meaning of life?",
                       "How tall is the Empire State Building?",
                       "What is the capital of France?"
                   ])

demo.launch()
