from base_loader import BaseLoader
import requests


class ProductLoader(BaseLoader):
    def load_request(self, item) -> requests.Response:
        re = self.himarket_api.product_post(item)
        print(re.content)
        return re


class StoreLoader(BaseLoader):
    def load_request(self, item) -> requests.Response:
        re = self.himarket_api.store_post(item)
        print(re.content)
        return re


class ConsumerLoader(BaseLoader):
    def load_request(self, item) -> requests.Response:
        re = self.himarket_api.consumer_post(item)
        print(re.content)
        return re
