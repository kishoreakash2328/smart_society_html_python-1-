from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

USERS = {
    "admin@gmail.com": "12345",
    "user@gmail.com": "password"
}

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if email in USERS and USERS[email] == password:
        return jsonify({"status": "success", "message": "Login Successful!"}), 200
    else:
        return jsonify({"status": "error", "message": "Invalid Email or Password!"}), 401

@app.route('/api/verify-otp', methods=['POST'])
def verify_otp():
    data = request.get_json()
    otp = data.get('otp')

    if otp == "1234":
        return jsonify({"status": "success", "message": "OTP Verified!"}), 200
    else:
        return jsonify({"status": "error", "message": "Invalid OTP!"}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)