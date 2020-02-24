import sys
import os
import json

from pydash import py_
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from driver.py_request import PyRequest



class GetSize:


    """
        use repository owner name and repo name to get size information
    """
    owner = ''
    repoName = ''

    def __init__(self, owner, repoName):

        self.owner = owner
        self.repoName = repoName



    def extract_values(self, obj, key):
        """Pull all values of specified key from nested JSON."""
        arr = []

        def extract(obj, arr, key):
            """Recursively search for values of key in JSON tree."""
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if isinstance(v, (dict, list)):
                        extract(v, arr, key)
                    elif k == key:
                        arr.append(v)
            elif isinstance(obj, list):
                for item in obj:
                    extract(item, arr, key)
            return arr

        results = extract(obj, arr, key)
        return results

    def get(self):
        response = PyRequest().get(f'https://api.github.com/repos/{self.owner}/{self.repoName}/events')
        #TODO: extract response json with useful data
        return  self.extract_values(response,'size')










# new_response = max(GetSize("twbs", "bootstrap").get())
# print(new_response)

