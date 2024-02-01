# Generative-AI
#Generative AI practise

In the ever-evolving landscape of artificial intelligence, the development of multimodal models has marked a pivotal moment. The quest for AI models capable of understanding and processing information from diverse sources has led to the evolution of multimodal AI. Google's Gemini, a testament to this evolution, represents a significant leap forward in addressing the complexities associated with different types of data—text, code, audio, images, and video.

To begin with, we need to install the Python programming language.

Install Python:

Download the latest Python version https://www.python.org/downloads/ compatible with your operating system.

During installation, check the box to add Python to PATH. This enables running Python from the command line.

Open a command prompt and verify the python installation by typing

Install Visual Studio Code:

Download Visual Studio Code from https://code.visualstudio.com/.

Run the installer and follow the instruction prompts. You can keep all the default setting during installation.

Open the Visual Studio Code and install the Python extension

 Install Anaconda:

Next we need to install Anaconda that helps to create and manage virtual environment(s) for different projects.

Download Anaconda for your operating system from https://www.anaconda.com/products/individual

Run the Anaconda installer and follow the installation prompts.

Creating a Conda Environment in VS Code:

Open the Command Palette again (Ctrl+Shift+P or Cmd+Shift+P).

Type "Python: Create Terminal" to open a terminal in VS Code or Select Terminal=> New Terminal from the menu bar of the  VS code

Install Gemini:

Within the activated environment, install Gemini using the command

pip install Gemini

Setup your Google API key

Vist Google AI studio https://makersuite.google.com/app/apikey to get your API key.

Testing the Setup

Create conda environment

Type the following command to create a virtual environment with conda  named "venv" inside a work folder.

conda create -n venv python=3.11  # Replace 3.8 with your desired Python version

The virtual environment is venv  in this case. Press “y” button whenever it asks you to proceed.

Activate the virtual environment using the below command:

conda activate venv

create .env file and store GOOGLE_API_KEY in it

create requirements.txt file and put the libraries in it

         google-generativeai

         python-dotenv

3. At terminal install these libraries using > pip install -r requirsments.txt

4.  create an geminiAI.py file and write all the code and then run the code using

python geminiAI.py command

# my first program 

import os

## GenerativeModel

 import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))  

## Function to load OpenAI model and get respones 

 def get_gemini_response(question):   

      model = genai.GenerativeModel('gemini-pro')   

    response = model.generate_content(question)     

    return response.text   

prompt = "Write a poem about a beautiful sunset." 

response = get_gemini_response(prompt) 

print(response)
