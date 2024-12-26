# app.py
from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

def check_password_strength(password):
    suggestions = []
    if len(password) < 8:
        suggestions.append("Password must be at least 8 characters long.")
    if not re.search("[a-z]", password):
        suggestions.append("Include at least one lowercase letter.")
    if not re.search("[A-Z]", password):
        suggestions.append("Include at least one uppercase letter.")
    if not re.search("[0-9]", password):
        suggestions.append("Include at least one digit.")
    if not re.search("[@#$%^&+=]", password):
        suggestions.append("Include at least one special character.")
    
    if suggestions:
        return "Weak: Password is weak.", suggestions
    return "Strong: Password is strong.", []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_password', methods=['POST'])
def check_password():
    password = request.form['password']
    strength, suggestions = check_password_strength(password)
    return jsonify({'strength': strength, 'suggestions': suggestions})

if __name__ == '__main__':
    app.run(debug=True)