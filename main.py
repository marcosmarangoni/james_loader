from api import HimarketApi
from json_loader import JsonLoader
from twisted.internet import task, reactor

tmp_products_array = []


def loop_thread():
    if tmp_products_array:
        product = tmp_products_array.pop(0)
        print(product)
    else:
        reactor.stop()


if __name__ == "__main__":
    himarket_api = HimarketApi()
    json_loader = JsonLoader()

    products = json_loader.get_products()

    for i in range(10):
        tmp_products_array.append(products[i])

    himarket_api.login()
    r = himarket_api.store_get()
    print(r.content)

    l = task.LoopingCall(loop_thread)
    l.start(1)
    reactor.run()
