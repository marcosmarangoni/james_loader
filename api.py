import requests
import json


class HimarketApi:
    BASE_URL = 'https://james.himarket.club:3000/api/v1'

    SALES_RECEIPT = '{base}/sales_receipt'.format(base=BASE_URL)
    STORES = '{base}/admin/stores'.format(base=BASE_URL)
    TOKEN = '{base}/token'.format(base=BASE_URL)
    PRODUCTS = '{base}/admin/products'.format(base=BASE_URL)
    CONSUMERS = '{base}/admin/consumers'.format(base=BASE_URL)
    RECEIPTS = '{base}/sales-receipt'.format(base=BASE_URL)

    def __init__(self):
        self.header = {}

    def login(self) -> requests.Response:
        data = {
            #"email": "api-coop@himarket.com",
            "email": "admin-public@himarket.club",
            "password": "qweqwe123"
        }
        re = requests.post(self.TOKEN, json=data)
        re.raise_for_status()
        token = json.loads(re.content)['token']
        self.header = {
            'Content-Type': 'application/json',
            "authorization": "Bearer " + token
        }
        print(self.header)
        return re

    def product_post(self, product) -> requests.Response:
        re = requests.post(
            self.PRODUCTS,
            json={
                "product": product
            },
            headers=self.header)
        return re

    def store_post(self, store) -> requests.Response:
        re = requests.post(
            self.STORES,
            json={
                "store": store
            },
            headers=self.header)
        return re

    def consumer_post(self, consumer) -> requests.Response:
        re = requests.post(
            self.CONSUMERS,
            json={
                "consumer": consumer
            },
            headers=self.header)
        return re

    def receipt_post(self, receipt) -> requests.Response:
        re = requests.post(
            self.RECEIPTS,
            json={
                "sales_receipt": receipt
            },
            headers=self.header)
        return re
