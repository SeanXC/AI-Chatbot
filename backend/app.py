import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for the Flask app

# Set your Hugging Face API token and model URL
API_URL = "https://api-inference.huggingface.co/models/gpt2"  # You can replace 'gpt2' with another model
headers = {"Authorization": f"Bearer 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"}

# Function to use Hugging Face API to generate a response
def chatbot_response(user_input):
    data = {"inputs": user_input}

    # Make a POST request to Hugging Face's API
    response = requests.post(API_URL, headers=headers, json=data)

    # Check if response is valid and return generated text
    if response.status_code == 200:
        return response.json()[0]["generated_text"]
    else:
        return "Sorry, something went wrong with the AI API."

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    # If user message is empty, return a default response
    if not user_message:
        return jsonify({"response": "Please send a message."})

    bot_response = chatbot_response(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
