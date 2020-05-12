import requests
import json


class HimarketApi:
    credentials = {
        "email": "api-coop@himarket.com",
        "password": "qweqwe123"
    }

    # Sample de Store Post
    store_post_json = {
        "store":
            {
                "external_ref": "himarket_100",
                "legal_name": "himarket teste 100",
                "trading_name": "AV",
                "document_number": "01234567890123",
                "full_adress": "Rua Himarket 123",
                "zip_code": "00000-000",
                "phone_number": "(12)3456-7890",
                "is_market": "true",
                "is_pharma": "false",
                "is_active": "false",
                "is_billed": "false",
                "address_number": "123"
            }

    }

    BASE_URL = 'https://james.himarket.club:3000/api/v1'

    SALES_RECEIPT = '{base}/sales_receipt'.format(base=BASE_URL)
    STORES = '{base}/admin/stores'.format(base=BASE_URL)
    TOKEN = '{base}/token'.format(base=BASE_URL)
    PRODUCTS = '{base}/admin/products'.format(base=BASE_URL)

    header = {}

    def login(self) -> requests.Response:
        data = {
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

    def store_get(self) -> requests.Response:
        re = requests.get(self.STORES, headers=self.header)
        return re

    def store_post(self, json_post) -> requests.Response:
        re = requests.post(self.STORES, json=json_post, headers=self.header)
        return re

    def product_post(self, product) -> requests.Response:
        re = requests.post(
            self.PRODUCTS,
            json={
                "product": {
                    "code": product['code'],
                    "name": product['name'],
                    "is_active": product['is_active'],
                    "ean": product['ean']
                }
            },
            headers=self.header)
        return re
