from flask import Flask,request
import math
from flask import jsonify
import json

app = Flask(__name__)


@app.route('/home',methods =['POST'])
def post():
	json_data=request.data
	print json_data
	jsonobj=json.loads(json_data)
	n=len(jsonobj['coordinates'])
	print n
	for point in jsonobj['coordinates']:
		print point['x']
		print point['y']
		print point['z']
	
	print jsonobj['coordinates[x[0]]']
	print jsonobj['coordinates[x[n-1]]']
	return "success"


def hello():
	x1=float(request.args['x1'])
	y1=float(request.args['y1'])
	z1=float(request.args['z1'])
	x2=float(request.args['x2'])
	y2=float(request.args['y2'])
	z2=float(request.args['z2'])
	print "x:",x1-x2
	x=57.2958*x1-57.2958*x2
	y=57.2958*y1-57.2958*y2
	z=57.2958*z1-57.2958*z2
	total=x**2+y**2+z**2
	total = abs(total)
	dot=(x1*x2)+(y1*y2)+(z1*z2)
	cross=(math.sqrt(x1**2+y1**2+z1**2))*(math.sqrt(x2**2+y2**2+z2**2))
	angle=abs(dot/cross)
	theta=math.acos(angle)
	degree=theta*180/math.pi
	num=(math.sqrt(total))
	return jsonify(distance=num,angle=degree)
	
if __name__ == "__main__":
	app.run(host= '128.82.8.12', port=8080, debug=False)
