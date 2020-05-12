import json


class JsonLoader:
    james_products_file = 'JamesProducts1.json'

    def get_products(self):
        with open(self.james_products_file) as james_products:
            products = json.load(james_products)
            products_array = []
            for product in products:
                product_obj = json.loads(product['product'])
                product_details = {"code": None, "name": None, "is_active": None, "ean": None}
                product_details['code'] = product_obj['code']
                product_details['name'] = product_obj['name']
                product_details['is_active'] = product_obj['is_active']
                product_details['ean'] = product_obj['ean']
                products_array.append(product_details)
            return products_array
