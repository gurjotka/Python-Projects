import requests
import json
import os
from dotenv import load_dotenv


def indian_product():
  load_dotenv()

  API_KEY = os.environ.get("DEEPSEEK_API_KEY_LLAMA")

  url = "https://api.fireworks.ai/inference/v1/chat/completions"
  headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
  }

  conversation_history = []

  print("Welcome to the Indian Product Checker! (Type 'exit' to quit.)")
  print("Give a Product Name...")

  while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
      break

    conversation_history.append({"role": "user", "content": f" Give answer in one sentence, Is {user_input} an Indian Product?"})

    payload = {
      "model": "accounts/fireworks/models/llama-v3p1-8b-instruct",
      "max_tokens": 16384,
      "top_p": 1,
      "top_k": 40,
      "presence_penalty": 0,
      "frequency_penalty": 0,
      "temperature": 0.6,
      "messages": conversation_history
    }

    try:
      response = requests.request("POST", url, headers=headers, data=json.dumps(payload)).json()

      assistant_message = response["choices"][0]["message"]["content"]
      print("Assistant:", assistant_message)

      conversation_history.append({"role": "assistant", "content": assistant_message})

    except Exception as e:
      print("An error occurred:", e)

indian_product()