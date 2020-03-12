import requests

class ApiRequest:

    def __init__(self,method,url,data=None,cookies=None,headers=None):
        try:
            if method=="get":
                self.resq=requests.get(url=url,params=data,cookies=None,headers=None)
            elif method=="post":
                self.resq = requests.post(url=url, data=data, cookies=None, headers=None)
            elif method=="delete":
                self.resq = requests.delete(url=url, params=data, cookies=None, headers=None)
        except Exception as e:
            raise e

    def get_status_code(self):
        return self.resq.status_code

    def get_text(self):
        return self.resq.text

    def get_json(self):
        return self.resq.json()
