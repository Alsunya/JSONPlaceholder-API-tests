import requests
import constants


class HttpClient:

    @staticmethod
    def get(path="/", params=None, headers=None):
        url = f"{constants.base_url}{path}"
        return requests.get(url=url, params=params, headers=headers)
