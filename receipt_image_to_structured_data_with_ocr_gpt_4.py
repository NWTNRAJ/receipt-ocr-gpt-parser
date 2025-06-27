!pip install pytesseract Pillow openai
!pip install openai==0.28
!apt-get install tesseract-ocr

from PIL import Image
import pytesseract
import openai
import io
import requests

from google.colab import files
uploaded = files.upload()
image_path = next(iter(uploaded))
image = Image.open(image_path)
image.show()

raw_text = pytesseract.image_to_string(image)
print("OCR Raw Text:\n", raw_text)

import openai
openai.api_key = "YOUR_API_KEY"

response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
    {"role": "system", "content": "You are a helpful assistant that extracts structured data from receipts in Label: Detail format."},
    {"role": "user", "content": f"Extract structured data from the following receipt text:\n\n{raw_text}"}
  ]
)

print(response['choices'][0]['message']['content'])


response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
    {"role": "system", "content": "You are a helpful assistant that extracts structured data from receipts in Label: Detail format."},
    {"role": "user", "content": f"Extract structured data from the following receipt text:\n\n{raw_text}"}
  ]
)

print(response['choices'][0]['message']['content'])

response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
    {"role": "system", "content": "You extract structured data from receipts in JSON format with keys like 'Store Name', 'Date', 'Items', 'Total', etc."},
    {"role": "user", "content": f"Convert the following receipt text to JSON:\n\n{raw_text}"}
  ]
)

json_output = response['choices'][0]['message']['content']
print("JSON Format:\n", json_output)
