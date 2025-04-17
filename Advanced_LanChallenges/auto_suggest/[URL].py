import json
import random
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/suggest', methods=['POST'])
def suggest():
    data = request.get_json()
    query = data.get('query', '')
    suggestions = generate_suggestions(query)
    return jsonify({'suggestions': suggestions})

def generate_suggestions(query):
    # Example logic for generating suggestions
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
    return [word for word in words if query.lower() in word.lower()]

if __name__ == '__main__':
    app.run(debug=True, port=8080)