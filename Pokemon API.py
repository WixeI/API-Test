import requests
print("Insira o nome do pokemon")
pokeName = input().lower()

response = requests.get("https://pokeapi.co/api/v2/pokemon/" + pokeName)
if response.status_code == 200:
    pokemon = response.json()

for x in range(len(pokemon['types'])):
   print(pokemon['types'][x]['type']['name'])

