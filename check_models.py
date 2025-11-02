import google.generativeai as genai

genai.configure(api_key="AIzaSyD4eAP1_to0pxgNVZ4BlJj8V1xE_mD8U7E")

print("Available models:")
for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(f"- {model.name}")