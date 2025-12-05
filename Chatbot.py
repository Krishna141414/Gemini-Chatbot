import os
import google.generativeai as genai

# get your API key
api_key = os.environ.get("GEMINI_API_KEY")

if api_key is None:
    print("Gemini API key not found. Please set GEMINI_API_KEY first.")
    exit()

# configure gemini
genai.configure(api_key=api_key)

# YOUR MODEL (works based on your list)
model = genai.GenerativeModel("models/gemini-2.5-pro")


# chat session
chat = model.start_chat(history=[])

print("Chatbot: Hello! Ask me anything. Type 'bye' to exit.\n")

while True:
    user = input("You: ")

    if user.lower() == "bye":
        print("Chatbot: Goodbye!")
        break

    try:
        response = chat.send_message(user)
        print("Chatbot:", response.text)

    except Exception as e:
        print("Chatbot: Error talking to Gemini.")
        print("Reason:", e)

