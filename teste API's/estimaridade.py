import requests

nome = input("Digite o seu nome: ")

api = f"https://api.agify.io?name={nome}"


api = requests.get(api)



if api.status_code == 200:
    idade_media = api.json()['age']
    print("A API respondeu corretamente. A idade média para o nome", nome, "é de", idade_media, "anos.")
else:
    print("A API não respondeu corretamente. Por favor, tente novamente mais tarde.")

# response = requests.get(api)
# print(response.json()['age'], "anos é a idade média para o nome", nome)