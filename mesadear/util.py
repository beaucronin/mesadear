from typing import Optional, Dict
import requests

BASE_URL = 'https://api.airtable.com/v0/'

class Connection(object):
    def __init__(self, app_id: str, apikey: Optional[str]):
        self.app_id = app_id
        self.apikey = apikey
    
    def retrieve_record(self, table_name: str, record_id: str) -> Dict:
        url = '{}{}/{}/{}'.format(BASE_URL, self.app_id, table_name, record_id)
        print(url)
        p = {
            'api_key': self.apikey
        }
        r = requests.get(url, params=p)
        if r.status_code != 200:
            print(r.status_code)
            print(r.text)
        return r.json()


def get_apikey(provided: str) -> str:
    apikey: str
    if provided:
        apikey = provided
    else:
        apikey = None

    return apikey

def create_connection(app_id: str, provided: str) -> Connection:
    apikey: str = get_apikey(provided)
    
    return Connection(app_id, apikey)
