
import os
import google.generativeai as genai
#import gemini

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load OpenAI model and get respones

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text


prompt = "Write a poem about a beautiful sunset."
response = get_gemini_response(prompt)
print(response)