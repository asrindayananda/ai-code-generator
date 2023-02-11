import requests
import os
import openai
# openai.organization = ""
# openai.api_key = os.getenv("")
# openai.api_key = ""
# print(openai.Model.list())
# https://platform.openai.com/docs/api-reference/authentication
# pip install openai
# need to setup credit card
# https://platform.openai.com/account/billing/overview
# set usage limits
# https://platform.openai.com/account/billing/limits

api_key = os.getenv("OPENAI")

import requests

def generate_code(prompt, api_key):
    endpoint = "https://api.openai.com/v1/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": "text-davinci-003",
        "prompt": prompt,
        "max_tokens": 100,
        "temperature": 0.5,
    }
    response = requests.post(endpoint, headers=headers, json=data)
    if response.status_code == 200:
        generated_code = response.json()["choices"][0]["text"].strip()
        print(f"Generated code: {generated_code}")
        return generated_code
    else:
        print(f"Request failed with status code {response.status_code}")
        print(f"Response text: {response.text}")
        return None

generate_code('python function to change string to integer', api_key)