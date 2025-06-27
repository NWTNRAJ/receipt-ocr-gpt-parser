# ✅ Receipt OCR + GPT-4 Parser – Structured Data from Images

🔍 **A Python prototype that converts receipt images into structured data using Tesseract OCR + OpenAI GPT-4 API.**  
Built and tested entirely in **Google Colab**, this demo extracts raw text from receipt images and outputs structured information in either **Label: Value** format or **JSON**.

## Google Colab Link
📎 https://colab.research.google.com/drive/1paY8-Rp1r8ZPHZw0eU2_D1sznpjLDDJ2?usp=sharing
---

## 📸 What the System Does

1. Upload a receipt image (e.g., `.jpg`, `.png`)
2. Extract raw text using **Tesseract OCR**
3. Send the raw text to **OpenAI’s GPT-4 API**
4. Receive structured output as:
   - ✅ Label: Value pairs
   - ✅ JSON for downstream use

---

## 💡 Use Cases

- ✅ Automated Expense Management
- ✅ Digital Bookkeeping
- ✅ Financial Document Scanning Apps
- ✅ Smart Receipt Readers / Mobile Scanning
- ✅ Invoice/Receipt Data Extraction Pipelines

---

## 🛠️ Tools & Libraries Used

| Tool | Purpose |
|------|---------|
| [Python (Colab)](https://colab.research.google.com/) | Quick prototyping |
| [pytesseract](https://github.com/madmaze/pytesseract) | OCR engine |
| [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) | Open-source OCR engine |
| [Pillow (PIL)](https://pillow.readthedocs.io/) | Image handling |
| [OpenAI GPT-4](https://platform.openai.com/docs/guides/gpt) | Text parsing & structuring |

---

## 🚀 How to Use (In Google Colab)

1. 📎 Open the Colab Notebook:
   [🔗 Click to open notebook](https://colab.research.google.com/drive/1paY8-Rp1r8ZPHZw0eU2_D1sznpjLDDJ2?usp=sharing)

2. 📤 Upload a receipt image file when prompted

3. 🔑 Set your OpenAI API Key:

   You'll need an API key from OpenAI. Get it from:
   👉 [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)

   Paste it in this line of the notebook:

   ```python
   openai.api_key = "your_openai_api_key_here"

## ▶️ Run the notebook cells in order to see:
OCR text output
GPT-4 structured output (Label & JSON)

## Required Installation
You can run this in Colab directly, but here's what gets installed:

!pip install pytesseract Pillow openai
!pip install openai==0.28
!apt-get install tesseract-ocr



---


