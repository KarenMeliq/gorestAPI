import requests
import json

from self import self


class GetUser:

    def getUser(self):
        response = requests.get('https://gorest.co.in/public-api/users')
        assert response.status_code == 200
        print(response.json())


user =  GetUser
user.getUser(self)