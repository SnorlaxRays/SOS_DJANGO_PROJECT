from SERVICE.models import User
from SERVICE.utility.DataValidator import DataValidator
from .BaseService import BaseService

class ForgetPasswordService(BaseService):
    
    def search(self,params):
        q = self.get_model().objects.filter()
        
        val = params.get('login_id',None)
        if(DataValidator.isNotNull(val)):
            q = q.filter(login_id = val)
            return q
        
    def get_model(self):
        return User
    
    