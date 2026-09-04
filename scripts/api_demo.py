import requests
import truststore

truststore.inject_into_ssl()

url = "https://jsonplaceholder.typicode.com/users/1"
response = requests.get(url, timeout=10)

data = response.json()
print(f"le statut code : {response.status_code}")
print(f"Nom de l'utilisateur : {data['name']}")