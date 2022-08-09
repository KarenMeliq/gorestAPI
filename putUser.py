import requests
import json
from createUser import CreateUser

from self import self


class PutUser:
    auth_token = CreateUser.auth_token
    hed = {'Authorization': 'Bearer ' + auth_token}



    def putUser(self):
        mydata = open("data_put.json", "r").read()
        response = requests.put("https://gorest.co.in/public-api/users/3076", mydata, self.hed)
        response_body = response.json()
        print(response_body)



putuser = PutUser;
putuser.putUser(self)