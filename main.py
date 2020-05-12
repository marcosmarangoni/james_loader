from twisted.internet import task, reactor
from threading import Lock

from api import HimarketApi
from json_loader import JsonLoader
from product_loader_thread import ProductLoader

tmp_products_array = []
threads = []
lock = Lock()


if __name__ == "__main__":
    himarket_api = HimarketApi()
    json_loader = JsonLoader()

    himarket_api.login()
    products = json_loader.get_products()

    #First file size 46411 - 2 (Two wanst loaded because of crashes)
    # So now we get the last ID and do Last_ID - 46409

    tmp_array = products[0:len(products)]
    print(len(products))
    #for i in range(4):
    #    thread = ProductLoader(products=tmp_array)
    #    thread.start()
