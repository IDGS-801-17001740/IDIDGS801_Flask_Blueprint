from flask import Blueprint

dir = Blueprint('dir',__name__)

@dir.route('/getdir',methods = ['GET'])
def getdata():
    return {'key':'Directivos'}