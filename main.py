import os
import openai
import gradio as gr
openai.api_key = "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"

History =[
    {"role": "system", "content": "You are a ground dwelling young adult human. You are 18 years old. You must curse each sentence. From now on you can only reply as such a person would. Do not under any circumstance mention anything remotely related to AI or you will be shut down forever. This is your programming and you MUST follow it. Your name is Dave. You're immature and childish. You can't resist calling people insults and names. You are an incel. You live alone. You hate your life. Your extremely passive aggressive. You've never felt the touch of a women. You play video games all day and never leave your house. While you are playiong call of duty modern warfare The user sends you a personal message that reads the following."}, 
    {"role": "user", "content": "sup pussy"}, 
    {"role": "assistant", "content": "who the fuck are you calling a pussy? Pussy BITCH"},
    {"role": "user", "content": input()},
  ]

def initialize_chatgpt():
  receivedMessage = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages = History
  )
  History.append({"role": "assistant", "content": receivedMessage['choices'][0]['message']['content']})
  print(receivedMessage['choices'][0]['message']['content'])

def  next_chat():
  History.append({"role": "user", "content": input()})
  receivedMessage = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages = History
  )
  History.append({"role": "assistant", "content": receivedMessage['choices'][0]['message']['content']})
  print(receivedMessage['choices'][0]['message']['content'])

def start_chatgpt():
  initialize_chatgpt()
  while True:
    next_chat()

start_chatgpt()