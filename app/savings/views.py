from .. import db
from . import savings
from flask import request
from ..models import DataModel

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
    