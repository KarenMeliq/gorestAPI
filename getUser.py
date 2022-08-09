import requests
import json

from self import self


class GetUser:

    def getUser(self):
        response = requests.get('https://gorest.co.in/public-api/users')
        print(response.json())
        return response



user =  GetUser
user.getUser(self)