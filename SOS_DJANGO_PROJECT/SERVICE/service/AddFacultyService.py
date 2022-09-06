from SERVICE.models import Faculty
from .BaseService import BaseService
from SERVICE.utility.DataValidator import DataValidator
from django.db import connection

'''
It contains Faculty business logics
'''
class AddFacultyService(BaseService):
    def get_model(self):
        return Faculty

    def search(self,params):
        print("Page No ---->",params['pageNo'])
        pageNo = (params['pageNo']-1) * self.pageSize
        sql = "select * from sos_faculty where 1=1"
        val = params.get("firstName", None)
        if (DataValidator.isNotNull(val)):
            sql += " and firstName = '"+val+"' "
        sql += " limit %s,%s"
        cursor = connection.cursor()
        print("---------------->",sql,pageNo,self.pageSize)
        params['index'] = ((params['pageNo'] - 1) * self.pageSize)+1
        cursor.execute(sql,[pageNo, self.pageSize])
        result = cursor.fetchall()
        columnName = ('id','firstName','lastName','email','password','address','gender','dob','college_ID','collegeName'
                    ,'subject_ID','subjectName','course_ID','courseName')
        res = {
            'data': [],
            "MaxId":1 # Using it through ORSAPI
        } 
        res["index"] = params["index"] # Using it through ORSAPI
        for x in result:
            # print({columnName[i]: x[i] for i,_ in enumerate(x)})
            res["MaxId"] = params['MaxId'] = x[0]
            res['data'].append({columnName[i]: x[i] for i,_ in enumerate(x)})
        return res
