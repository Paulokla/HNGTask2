Number Properties API

This API provides interesting mathematical properties and a fun fact about a given number.

## Endpoint

**GET** `/api/classify-number?number=<number>`

### Request

GET /api/classify-number?number=371

### Example Response (200 OK)

{
"number": 371,
"is_prime": false,
"is_perfect": false,
"properties": ["armstrong", "odd"],
"digit_sum": 11,
"fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}

Example Response (400 Bad Request)
{
"number": "alphabet",
"error": true
}

Deployment
The API is deployed on Render and can be accessed at:
(https://hngtask2-t9lr.onrender.com/api/classify-number/371)

Local Setup
Clone the repository:

git clone "https://github.com/Paulokla/HNGTask2.git"
cd number-properties-api

Set up a virtual environment:

python3 -m venv venv
source venv/bin/activate

Install dependencies:

pip install flask flask-cors
Run the application:

python API2.py
Access the API at http://127.0.0.1:5000/api/classify-number/371
