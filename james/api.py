import requests
import json


class JamesApi:
    BASE_URL = 'https://2mkl0vc3k8.execute-api.us-west-2.amazonaws.com/test/v1'

    RECEIPTS = '{base}/orders'.format(base=BASE_URL)

    def __init__(self):
        self.header = {
            'Content-Type': 'application/json',
            'x_api_key': 'MLnBFQUSj87HBQ42PI97n44pg9zglPzb4GzGIWB0'
        }

    def receipt_get(self, next) -> requests.Response:
        re = requests.get(
            url=self.RECEIPTS,
            params={
                "next": next
            },
            headers=self.header)
        return re
