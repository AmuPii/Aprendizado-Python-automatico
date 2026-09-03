import requests 

api = requests.get("https://dog.ceo/api/breeds/image/random")




if api.status_code == 200:
    link = api.json()['message']
    print(f"A API respondeu corretamente. Aqui está a imagem de um cachorro aleatório: {link}")
else:
    print("A API não respondeu corretamente. Por favor, tente novamente mais tarde.")

# response = requests.get(api)
# print(response.json()['message'])


