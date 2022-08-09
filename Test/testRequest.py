import pytest
from getUser import GetUser
from createUser import CreateUser
from putUser import PutUser

class testRequest:

    def testGetUser(self):
           response = GetUser.getUser()
           assert response.status_code == 200

    def testCreateUser(self):
        resp_body = CreateUser.cretaeUser()
        assert resp_body["code"] == 201

    def testPutUser(self):
        resp_body = PutUser.putUser()
        assert resp_body["code"] == 200