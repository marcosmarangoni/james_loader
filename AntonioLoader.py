import pandas as pd
import numpy as np
import json
from time import time
import itertools
import random
import mysql.connector
from datetime import datetime

if __name__ == "__main__":
    cnx = mysql.connector.connect(user='adviniski', password='h1market#2018',
                                  host='127.0.0.1',
                                  database='james')
    cursor = cnx.cursor()

    now = datetime.now()
    start_date = now.strftime("%d/%m/%Y, %H:%M:%S")
    print(start_date)

    print("Reading JSON!!")

    with open("data_files/venda_202005150856.json", "r") as file:
        data = json.load(file)

    query = "SELECT id FROM transactions"
    cursor.execute(query)
    records_transactions = cursor.fetchall()
    transactions = set([t[0] for t in records_transactions])

    # print(random.sample(transactions, 10))

    query = "SELECT id FROM stores"
    cursor.execute(query)
    records_stores = cursor.fetchall()
    stores = set([s[0] for s in records_stores])

    # print(random.sample(stores, 10))

    query = "SELECT ean FROM products"
    cursor.execute(query)
    records_products = cursor.fetchall()
    products = set([p[0] for p in records_products])

    # print(random.sample(products, 10))

    query = "SELECT id FROM consumers"
    cursor.execute(query)
    records_consumers = cursor.fetchall()
    consumers = set([c[0] for c in records_consumers])

    # print(random.sample(consumers, 10))

    query = "SELECT ean, price FROM items"
    cursor.execute(query)
    record_items = cursor.fetchall()
    inserted_items = set(record_items)

    # print(random.sample(inserted_items, 10))

    print("Start de insertion of %d transactions!" % (len(data)))

    count_c = 0
    count_t = 0
    count_s = 0
    count_p = 0
    count_i = 0
    count_ci = 0

    for index, json_string in enumerate(data):

        json_data = json.loads(json_string["json_build_object"])
        transaction_id = json_data["external_ref"]

        if (transaction_id not in transactions):
            store_id = int(json_data["store_external_ref"])
            if (store_id not in stores):
                count_s += 1
                stores.add(store_id)

            consumer = json_data["consumer"]
            consumer_id = int(consumer["external_ref"])
            if (consumer_id not in consumers):
                count_c += 1
                consumers.add(consumer_id)

            sales_receipts = json_data["sales_receipt_items"]
            for item in sales_receipts:
                ean = item["ean"]
                price = item["unity_price"]

                if (ean is not None and price > 0):

                    if (ean not in products):
                        count_p += 1
                        products.add(ean)

                    if ((ean, price) not in inserted_items):
                        count_i += 1
                        inserted_items.add((ean, price))

                    count_ci += 1

            count_t += 1
            transactions.add(transaction_id)

        if (index % 10000 == 0):
            print("Analysed %d transactions" % (index))

    print("Consumers to insert: %d" % (count_c))
    print("Transactions to insert: %d" % (count_t))
    print("Stores to insert: %d" % (count_s))
    print("Products to insert: %d" % (count_p))
    print("Items to insert: %d" % (count_i))
    print("Commercialized_items to insert: %d" % (count_ci))

    consumers_insert = np.empty(count_c, dtype=object)
    transactions_insert = np.empty(count_t, dtype=object)
    products_insert = np.empty(count_p, dtype=object)
    stores_insert = np.empty(count_s, dtype=object)
    items_insert = np.empty(count_i, dtype=object)
    commercialized_items = np.empty(count_ci, dtype=object)

    del transactions
    del stores
    del products
    del consumers
    del inserted_items

    transactions = set([t[0] for t in records_transactions])
    stores = set([s[0] for s in records_stores])
    products = set([p[0] for p in records_products])
    consumers = set([c[0] for c in records_consumers])
    inserted_items = set(record_items)

    co = 0
    tr = 0
    st = 0
    pr = 0
    it = 0
    ci = 0

    for index, json_string in enumerate(data):

        json_data = json.loads(json_string['json_build_object'])
        transaction_id = json_data["external_ref"]

        if (transaction_id not in transactions):
            store_id = int(json_data["store_external_ref"])
            if (store_id not in stores):
                stores_insert[st] = (store_id, None)
                stores.add(store_id)
                st += 1

            consumer = json_data["consumer"]
            consumer_id = consumer["external_ref"]
            if (consumer_id not in consumers):
                consumers_insert[co] = (consumer_id, consumer["name"], consumer["document"])
                consumers.add(consumer_id)
                co += 1

            sales_receipts = json_data["sales_receipt_items"]
            discount = float(0.0)

            for item in sales_receipts:
                ean = item["ean"]
                price = item["unity_price"]
                qnt = item["qnt"]
                name = item["name"]

                if (ean is not None and price > 0):
                    if (ean not in products):
                        products_insert[pr] = (ean, name, None, None, None)
                        products.add(ean)
                        pr += 1

                    new_item = (ean, price)

                    if (new_item not in inserted_items):
                        items_insert[it] = new_item
                        inserted_items.add(new_item)
                        it += 1

                    commercialized_items[ci] = (item["sale_external_ref"], new_item, qnt)
                    ci += 1

                elif (price is not None and price < 0 and ean is None and name == "Desconto aplicado no caixa"):
                    discount = abs(price)

            transactions_insert[tr] = (transaction_id,
                                       store_id,
                                       consumer_id,
                                       json_data["issue_date"],
                                       json_data["comercialized_itens"],
                                       json_data["purchase_total"],
                                       discount,
                                       json_data["doct_number"],
                                       json_data["payment_method"])

            transactions.add(transaction_id)
            tr += 1
        if (index % 10000 == 0):
            print("Inserting/updating %d transactions" % (index))

    print(tr)
    print(st)
    print(pr)
    print(co)
    print(it)

    query = " INSERT INTO stores (id, name) VALUES (%s, %s) ON DUPLICATE KEY UPDATE id = VALUES(id)"
    cursor.executemany(query, list(stores_insert))
    cnx.commit()

    print("Stores inserted!!")
    cnx.commit()
    split_data = np.array_split(products_insert, 40)
    query = "INSERT INTO products (ean, name, slug, brand_id, category_id) VALUES (%s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE ean = VALUES(ean)"
    for split in split_data:
        cursor.executemany(query, list(split))
        cnx.commit()

    print("Products inserted!!")
    cnx.commit()
    split_data = np.array_split(consumers_insert, 50)
    query = "INSERT INTO consumers (id, name, personal_code) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE id = VALUES(id)"
    for split in split_data:
        cursor.executemany(query, list(split))
        cnx.commit()

    print("Consumers inserted!!")
    cnx.commit()
    split_data = np.array_split(transactions_insert, 100)
    query = "INSERT INTO transactions (id," \
            "store_id," \
            "consumer_id," \
            "issue_date," \
            "commercialized_items," \
            "purchase_total," \
            "discount," \
            "doct_number," \
            "payment_method)" \
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)" \
            "ON DUPLICATE KEY UPDATE id = VALUES(id)"
    for split in split_data:
        cursor.executemany(query, list(split))
        cnx.commit()

    print("Transactions Inserted!!")
    cnx.commit()
    split_data = np.array_split(items_insert[0:it], 200)
    query = "INSERT INTO items (ean, price) VALUES (%s, %s) ON DUPLICATE KEY UPDATE price = VALUES(price)"
    for split in split_data:
        cursor.executemany(query, list(split))
        cnx.commit()

    print("Items Inserted!!")
    cnx.commit()

    query = "SELECT id, ean, price  FROM items"

    cursor.execute(query)
    record = cursor.fetchall()

    search_data = {}

    for r in record:
        search_data[(r[1], r[2])] = r[0]

    commercialized_items_insert = np.empty(count_ci, dtype=object)

    for i, item_transaction in enumerate(commercialized_items):
        item_id = search_data[item_transaction[1]]
        transaction_id = item_transaction[0]
        qnt = item_transaction[2]
        commercialized_items_insert[i] = (transaction_id, item_id, qnt)

    split_data = np.array_split(commercialized_items_insert, 300)
    query = "INSERT INTO commercialized_items (transaction_id, item_id, quantity) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE id = VALUES(id)"

    for split in split_data:
        cursor.executemany(query, list(split))
        cnx.commit()

    print("Commercialized Items in Transaction Inserted!!")

    cnx.commit()
    cursor.close()
    cnx.close()

    now = datetime.now()
    end_date = now.strftime("%d/%m/%Y, %H:%M:%S")

    print("Start: " + start_date)
    print("End: " + end_date)
