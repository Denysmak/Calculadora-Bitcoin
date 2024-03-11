import requests

def get_bitcoin_price():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=brl'
    response = requests.get(url)
    data = response.json()
    bitcoin_price = data['bitcoin']['brl']
    return bitcoin_price
bitcoin_price = get_bitcoin_price()
valorComprado = float(input('Quantos reais você comprou? '))
valorBitcoin = float(input('Qual era o valor do bitcoin na hora da compra? '))
qtdBitcoin = str(1/(valorBitcoin/valorComprado))
print("Você comprou "+ qtdBitcoin + " de bitcoin.")
print(qtdBitcoin + " equivale a " + str(float(qtdBitcoin)*bitcoin_price) + " reais hoje em dia")

