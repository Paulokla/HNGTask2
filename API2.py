from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# Utility Functions
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_armstrong(num):
    digits = [int(d) for d in str(num)]
    power = len(digits)
    return num == sum(d ** power for d in digits)

def is_perfect(num):
    return num > 0 and sum(i for i in range(1, num // 2 + 1) if num % i == 0) == num


@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number_param = request.args.get("number")

    if not number_param or not number_param.isdigit():
        return jsonify({"number": number_param, "error": True}), 400

    number = int(number_param)
    properties = []

    if is_armstrong(number):
        properties.append("armstrong")
    properties.append("odd" if number % 2 != 0 else "even")

    try:
        fun_fact = requests.get(NUMBERS_API_URL.format(number)).text
    except requests.RequestException:
        fun_fact = "No fun fact available."

    response = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": sum(int(d) for d in str(number)),
        "fun_fact": fun_fact
    }

    return jsonify(response), 200


if __name__ == '__main__':
    app.run(debug=True)
