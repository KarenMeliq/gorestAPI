import requests
import json
from createUser import CreateUser

from self import self


class PutUser:

    def putUser(self):
        auth_token = CreateUser.auth_token
        hed = {'Authorization': 'Bearer ' + auth_token}
        mydata = open("D:\pythonProject\data_put.json", "r").read()
        response = requests.put("https://gorest.co.in/public-api/users/5148", mydata, headers=hed)
        response_body = response.json()
        print(response_body)
        return response_body



putuser = PutUser;
putuser.putUser(self)