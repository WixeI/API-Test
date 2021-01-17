import requests

response = requests.get("https://randomfox.ca/floof/")
print(response.status_code) #Resposta da tentativa de pegar dados do link. 200 é OK. Ver HTTPs codes para mais.

fox = response.json()
print(fox.keys())
print(fox['image'])

