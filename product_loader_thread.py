from threading import Thread, Lock
import time
from api import HimarketApi


class ProductLoader(Thread):
    def __init__(self, products):
        super().__init__()
        self.products = products
        self.lock = Lock()
        self.himarket_api = HimarketApi()
        self.himarket_api.login()

    def run(self) -> None:
        while self.products:
            product = {}
            with self.lock:
                product = self.products.pop(0)
            re = self.himarket_api.product_post(product)
            print(re.content)
            time.sleep(0.1)

