import truststore
truststore.inject_into_ssl()

import requests


url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.delete(url, timeout=10)
print(response.status_code)
print(response.text)
