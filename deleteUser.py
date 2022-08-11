import requests
import json
from self import self

class DeleteUser:


    def deletUser(self):
        auth_token = '148d7b37e7c7a851e567f048cc32b93e98c5feaa22905d54db0146cace778845'
        hed = {'Authorization': 'Bearer ' + auth_token}
        response = requests.delete("https://gorest.co.in/public-api/users/3076", headers=hed)
        response_body = response.json()
        print(response_body)


user = DeleteUser
user.deletUser(self)