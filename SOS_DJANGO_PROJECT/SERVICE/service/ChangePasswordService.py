from collections import UserList
from SERVICE.models import User
from SERVICE.utility.DataValidator import DataValidator
from .BaseService import BaseService

class ChangePasswordService(BaseService):
    
    def authenticate(self,params):
        userList = self.search(params)
        if( userList.count() > 0):
            print("8888888->", userList[0].login_id)
            return userList[0]
        else:
            return None

        
    def get_model(self):
        return User

        