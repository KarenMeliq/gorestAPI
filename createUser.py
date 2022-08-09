import requests
import json

from self import self


class CreateUser:
    auth_token = '148d7b37e7c7a851e567f048cc32b93e98c5feaa22905d54db0146cace778845'
    def cretaeUser(self):
        auth_token = '148d7b37e7c7a851e567f048cc32b93e98c5feaa22905d54db0146cace778845'
        hed = {'Authorization': 'Bearer ' + auth_token}
        mydata = open("D:\pythonProject\data.json", "r").read()
        response = requests.post("https://gorest.co.in/public-api/users", data=json.loads(mydata), headers=hed)
        response_body = response.json()
        print(response_body)
        return response_body


user = CreateUser
user.cretaeUser(self)