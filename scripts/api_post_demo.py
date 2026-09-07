import truststore
truststore.inject_into_ssl()

import requests


url = "https://jsonplaceholder.typicode.com/posts"
payload = {
    "title": "My first API post",
    "body": "Created during QA Automation learning",
    "userId": 1,
}

response = requests.post(url, json=payload, timeout=10)
print(response.status_code)
print(response.json())
