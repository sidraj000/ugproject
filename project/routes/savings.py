from project.extensions import db
from flask import request,Blueprint
from project.models import DataModel

savings=Blueprint('savings',__name__)
@savings.route('/data/health',methods=['GET'])
def msg():
        return{"msg":"healthy"}

@savings.route('/data/show',methods=['GET'])
def showsavings():
        savingsdata=db.session.query(DataModel)
        data={}
        j=0
        for i in savingsdata:
             data[j]=("cordinate is "+i.cordinates)
             j+=1
        return data
@savings.route('/data/add', methods=['POST'])
def retiral_submission():
     data =  request.get_json(force=True)
     cordinates=(data['Cordinate'])
     newData = DataModel(cordinates=cordinates)
     db.session.add(newData)
     db.session.commit()

  
     return {"msg":"data added successfully"}
    
