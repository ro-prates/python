# algoritmo que devolve a cotação do dólar, euro e do bitcoin
import requests

cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
cotacoes = cotacoes.json()
dolar = cotacoes['USDBRL']['bid']
print(f'valor dólar: R${float(dolar):.2f}')

euro = cotacoes['EURBRL']['bid']
print(f'valor euro: R${float(euro):.2f}')

bitcoin = cotacoes['BTCBRL']['bid']
print(f'valor bitcoin: R${float(bitcoin):.2f}')