from binance import Client

from data.config import API_KEY, API_SECRET
from utils.misc.dollar_rate import get_currency_price

client = Client(api_key=API_KEY, api_secret=API_SECRET)
dollar = get_currency_price()


def get_address_btc():
    address = client.get_deposit_address(coin='BTC')['address']
    return address


def get_address_eth():
    address = client.get_deposit_address(coin='ETH')['address']
    return address


def get_address_sol():
    address = client.get_deposit_address(coin='SOL')['address']
    return address


def get_btc_course():
    avg_price = client.get_avg_price(symbol='BTCBUSD')
    btc_price = float(avg_price['price'])
    rub = dollar * btc_price
    return round(rub)


def get_eth_course():
    avg_price = client.get_avg_price(symbol='ETHBUSD')
    eth_price = float(avg_price['price'])
    rub = dollar * eth_price
    return round(rub)


def get_sol_course():
    avg_price = client.get_avg_price(symbol='SOLBUSD')
    sol_price = float(avg_price['price'])
    rub = dollar * sol_price
    return round(rub)
