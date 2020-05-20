from json_reader import JsonReader
from loaders import ProductLoader, StoreLoader, ConsumerLoader
from api import HimarketApi


def load_products():
    products = JsonReader.get_products()

    # First file size 46411 - 2 (Two wanst loaded because of crashes)
    # So now we get the last ID and do Last_ID - 46409
    tmp_array = products[0:len(products)]
    print(len(products))

    for i in range(2):
        thread = ProductLoader(array=tmp_array)
        thread.start()


def load_stores():
    stores = JsonReader.get_stores()
    tmp_stores = stores[0:len(stores)]
    print(len(stores))

    for i in range(4):
        thread = StoreLoader(array=tmp_stores)
        thread.start()


def load_people():
    people = JsonReader.get_consumers()
    tmp_people = people[0:len(people)]
    print(len(people))

    for i in range(4):
        thread = ConsumerLoader(array=tmp_people)
        thread.start()


def test():
    himarket_api = HimarketApi()
    himarket_api.login()
    people = JsonReader.get_consumers()
    person = people[0]
    re = himarket_api.consumer_post(person)
    print(re.content)


if __name__ == "__main__":
    load_people()
