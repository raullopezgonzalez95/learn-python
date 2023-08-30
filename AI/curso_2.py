# Create AI Image Using Python

import openai
openai.api_key = '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'
openai.Model.list()

import requests
from PIL import Image

def generate(text):
    res = openai.Image.create(
        prompt=text,
        n=1,
        size="256x256",
    )
    return res["data"][0]["url"]

text = "create a batman art"
url1 = generate(text)
response = requests.get(url1)
Image.open(response.raw)
