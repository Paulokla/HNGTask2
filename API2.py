from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

NUMBERS_API_URL = "http://numbersapi.com/{}/math"

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def digit_sum(n):
    return sum(int(digit) for digit in str(abs(n)))


def is_perfect(n):
    if n <= 0:
        return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n


def is_armstrong(n):
    num_str = str(abs(n))
    return n == sum(int(digit) ** len(num_str) for digit in num_str)


def get_fun_fact(number):
    try:
        response = requests.get(NUMBERS_API_URL.format(number))
        return response.text if response.status_code == 200 else "No fact available"
    except requests.RequestException:
        return "No fact available"


@app.route("/api/classify-number", methods=["GET"])
def classify_number():
    number_param = request.args.get("number")

    if number_param is None or number_param.strip() == "":
        return jsonify({"error": True, "number": ""}), 400

    try:
        number = int(number_param)
    except ValueError:
        return jsonify({"error": True, "number": number_param}), 400

    response_data = {
        "error": False,
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "digit_sum": digit_sum(number),
        "properties": [],
        "fun_fact": get_fun_fact(number)
    }

    if number % 2 == 0:
        response_data["properties"].append("even")
    else:
        response_data["properties"].append("odd")

    if is_armstrong(number):
        response_data["properties"].append("armstrong")

    return jsonify(response_data), 200


if __name__ == "__main__":
    app.run(debug=True)
