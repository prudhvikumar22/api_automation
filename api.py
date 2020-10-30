try:
    import requests
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
    import json
    import pprint
except Exception as e:
    print("Module might be missing, See the message----> ", e)

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class Api:
    def __init__(self, ip, port, token):
        self.ip = ip
        self.port = port
        self.token = token
        self.head = {'Authorization': 'Bearer ' + self.token, 'Content-type': 'application/json'}
        self.url = 'https://' + self.ip + ':' + self.port

    def get(self, api_to_execute):
        r = requests.get(self.url + api_to_execute, headers=self.head, verify=False)
        if r.status_code != 200:
            r.json()
        else:
            return r

    def post(self, api_to_execute, payload):
        r = requests.post(self.url + api_to_execute, data=json.dumps(payload), headers=self.head, verify=False)
        if r.status_code != 200:
            r.json()
        else:
            return r

    def put(self, api_to_execute, payload):
        r = requests.put(self.url + api_to_execute, data=json.dumps(payload), headers=self.head, verify=False)
        if r.status_code != 200:
            r.json()
        else:
            return r

    def delete(self, api_to_execute):
        r = requests.delete(self.url + api_to_execute, headers=self.head, verify=False)
        if r.status_code != 200:
            r.json()
        else:
            return r



