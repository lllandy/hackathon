from bottle import route, run, request, get
from bottle import static_file
#from ... import ....

@route('/<filename>')
def server_static(filename):
    return static_file(filename, root='./')

@get('/login')
def getRecommanded():
	v = request.forms.get("recBtn")
	print(v)


# def getRecommanded(userLocation, resturantInfos):
# 	def getLocation(resturantInfo) :
# 		resturantInfo.location
# 	resturantLocations = map(getLocation, resturantInfos)
# 	indexes ....(userLocation, resturantLocations);
# 	return 


run(host='localhost', port=8080, debug=True)