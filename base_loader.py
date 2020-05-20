from abc import abstractmethod
from threading import Thread, Lock
import requests
import time

from requests import Request

from api import HimarketApi


class BaseLoader(Thread):
    def __init__(self, array):
        super().__init__()
        # Used to store the Himarket api endpoints
        self.himarket_api = HimarketApi()
        # Used to lock the thread
        self.lock = Lock()

        self.array = array
        self.himarket_api.login()

    @abstractmethod
    def load_request(self, item) -> requests.Response:
        pass

    def run(self) -> None:
        while self.array:
            # Lock the thread while popping the item
            with self.lock:
                item = self.array.pop(0)

            self.load_request(item=item)
            # time.sleep(0.1)
