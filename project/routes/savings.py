from project.extensions import db
from flask import request,Blueprint,jsonify
from project.models import DataModel
from project.models import SensorData


savings=Blueprint('savings',__name__)
@savings.route('/data/health',methods=['GET'])
def msg():
        return{"msg":"healthy"}

@savings.route('/data/show',methods=['GET'])
def showsavings():
        savingsdata=db.session.query(SensorData)
        data=[]
        for i in savingsdata:
             data.append({"sensorId":i.device_id,"data":i.sData,"time":i.timestamp})
        return jsonify(data)
@savings.route('/data/add', methods=['POST'])
def retiral_submission():
     data =  request.get_json(force=True)
     device_id=(data['DId'])
     sData=(data['sData'])
     newData = SensorData(device_id=device_id,sData=sData)
     db.session.add(newData)
     db.session.commit()

  
     return {"msg":"data added successfully"}
    
