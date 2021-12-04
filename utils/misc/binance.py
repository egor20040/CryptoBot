from binance import Client

from data.config import API_KEY, API_SECRET
from utils.misc.dollar_rate import get_currency_price


class StockExchange:
    client = Client(api_key=API_KEY, api_secret=API_SECRET)
    dollar = get_currency_price()

    def get_address(self, coin):
        address = self.client.get_deposit_address(coin=coin)['address']
        return address

    def get_course(self, coin):
        avg_price = self.client.get_avg_price(symbol=f'{coin}BUSD')
        btc_price = float(avg_price['price'])
        rub = self.dollar * btc_price
        return round(rub)
