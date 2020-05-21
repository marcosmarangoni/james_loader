from json_reader import JsonReader
from loaders import ProductLoader, StoreLoader, ConsumerLoader, ReceiptsLoader
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
    # 543 stores
    stores = JsonReader.get_stores()
    tmp_stores = stores[0:len(stores)]
    print(len(stores))

    for i in range(4):
        thread = StoreLoader(array=tmp_stores)
        thread.start()


def load_people():
    # 1168169 people
    people = JsonReader.get_consumers()
    tmp_people = people[0:len(people)]
    print(len(people))

    for i in range(4):
        thread = ConsumerLoader(array=tmp_people)
        thread.start()


def load_receipts():
    # 449798 receipts - First file
    receipts = JsonReader.get_receipts()
    tmp_receipts = receipts[0:len(receipts)]
    print(len(receipts))

    for i in range(10):
        thread = ReceiptsLoader(array=tmp_receipts)
        thread.start()


def test():
    himarket_api = HimarketApi()
    himarket_api.login()
    dummy = JsonReader.get_receipts()
    dummy_item = dummy[0]
    re = himarket_api.receipt_post(dummy_item)
    print(re.content)


if __name__ == "__main__":
    load_receipts()
