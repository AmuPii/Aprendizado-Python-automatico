import requests 

Moeda = "brl"

valor = float(input("Digite o valor em brl: "))

url = f"https://economia.awesomeapi.com.br/last/USD-BRL"

ValorDolar = requests.get(url).json()['USDBRL']['bid']

if Moeda == "brl":
    valorConvertido = valor / float(ValorDolar)
    print(f"O valor de {valor} BRL convertido para USD é: {valorConvertido:.2f} USD")


if requests.get(url).status_code != 200:
    print("A API não respondeu corretamente. Por favor, tente novamente mais tarde.")



# resposta = requests.get(url)
# print(resposta.json())