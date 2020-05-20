import json


class JsonReader:
    @staticmethod
    def get_products():
        with open('json_files/james_products_1.json') as file_products:
            products = json.load(file_products)
            products_array = []
            for product in products:
                product_obj = json.loads(product['product'])
                product_details = {'code': product_obj['code'],
                                   'name': product_obj['name'],
                                   'is_active': product_obj['is_active'],
                                   'ean': product_obj['ean']}
                products_array.append(product_details)
            return products_array

    @staticmethod
    def get_stores():
        with open('json_files/stores.json') as file_stores:
            stores = json.load(file_stores)
            stores_array = []
            for store in stores:
                store_obj = json.loads(store['json_build_object'])
                store_details = {'created_at': store_obj['created_at'],
                                 'external_ref': store_obj['external_ref'],
                                 'legal_name': store_obj['legal_name'],
                                 'trading_name': store_obj['trading_name'],
                                 'is_market': store_obj['is_market?'],
                                 'is_pharma': store_obj['is_pharma?'],
                                 'is_billed': store_obj['is_billed'],
                                 'address': store_obj['address'],
                                 'is_active': store_obj['is_active'],
                                 'latitude': store_obj['latitude'],
                                 'longitude': store_obj['longitude'],
                                 'full_address': store_obj['full_addres'],
                                 'address_number': store_obj['address_number'],
                                 'zip_code': str(store_obj['zip_code'])}

                stores_array.append(store_details)
            return stores_array

    @staticmethod
    def get_consumers():
        with open('json_files/people.json') as file_people:
            people = json.load(file_people)
            people_array = []
            for person in people:
                person_obj = json.loads(person['users'])
                person_details = {
                    "first_name": person_obj['first_name'],
                    "last_name": person_obj['last_name'],
                    "external_ref": person_obj['id'],
                    "document_number": '{doct}0000000000'.format(doct=person_obj['id']),
                    "document_type": 1
                }
                people_array.append(person_details)
            return people_array

    @staticmethod
    def get_receipts():
        with open('json_files/receipts.json') as file_receipts:
            receipts = json.load(file_receipts)
            receipts_array = []
            for receipt in receipts:
                receipt_obj = json.loads(receipt['json_build_object'])
                consumer_obj = json.loads(receipt_obj['consumer'])
                receipt_items = json.loads(receipt_obj['sales_receipt_items'])

                consumer_details = {
                    "name": consumer_obj['name'],
                    "document": consumer_obj['document'],
                    "external_ref": consumer_obj['external_ref']
                }

                receipt_item_array = []
                for receipt_item in receipt_items:
                    receipt_item_obj = json.loads(receipt_item)
                    receipt_item_details = {
                        "sale_external_ref": None,
                        "qnt": None,
                        "name": None,
                        "ean": None,
                        "unity_price": None
                    }
                    receipt_item_array.append(json.loads(receipt_item))

                receipt_details = {"external_ref": receipt_obj['external_ref'],
                                   "store_external_ref": receipt_obj['store_external_ref'],
                                   "is_active": receipt_obj['is_active'],
                                   "doct_number": receipt_obj['doct_number'],
                                   "issue_date": receipt_obj['issue_date'],
                                   "purchase_total": receipt_obj['purchase_total'],
                                   "paid_value": receipt_obj['paid_value'],
                                   "payable_amount": receipt_obj['payable_amount'],
                                   "comercialized_itens": receipt_obj['comercialized_itens'],
                                   "payment_method": receipt_obj['payment_method'],
                                   "consumer": consumer_details,
                                   "sales_receipt_items": receipt_item_array}
                receipts_array.append(receipt_details)
            return receipts_array
