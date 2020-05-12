from threading import Thread, Lock
from api import HimarketApi


class ProductLoader(Thread):
    def __init__(self):
        super().__init__()
        self.product = {}
        self.busy = False
        self.api = HimarketApi()
        self.lock = Lock()

    def run(self) -> None:
        if self.product:
            with self.lock:
                self.busy = True
            self.api.product_post(self.product)
            with self.lock:
                self.busy = False
