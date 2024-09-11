# The `requests` module in Python is a powerful library used for making HTTP requests. It simplifies the process of sending various types of HTTP requests (such as GET, POST, PUT, DELETE) and handling the responses. This module provides a more user-friendly interface compared to the standard library's `urllib`. It's widely used for interacting with web APIs, fetching web pages, and performing various web-related tasks in Python

import requests

# Sending a GET request
response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

# Checking the status code of the response
if response.status_code == 200:
    # Printing the response content
    print(response.json())
else:
    print("Error:", response.status_code)