
from sklearn.neighbors import NearestNeighbors
import numpy as np
import math
from random import randint
import api
import item_colab as rec_sys




# price range [1-5]

# food type: 
# 	Indian 0
# 	Paki 1
# 	..

# Location [long, lat] -> dist 




# Details
# Name 
# Contacts
# Ratings : get Avg 


# all_categories = set(projects[:, 5]) # get all unique categories 
# 	for cat in [0, 1, 2, 3, 4][:-1] : # create dummy variable for all but last category and append to the project features
# 		new_var = [1 if c == cat else 0 for c in projects[:, 5]]
# 		new_var = np.array(new_var)
# 		new_var = np.reshape(new_var, (new_var.shape[0], 1)) 
# 		project_X = np.concatenate((project_X, new_var), axis=1)





# X = np.array([[ 5,  3,  4, 4,  0],
#        [ 3,  1,  2,  3,  3],
#        [ 4,  3,  4,  3,  5],
#        [ 3,  3,  1,  5,  4],
#        [ 1, 5,  5,  2,  1]])


# rests = []

# location = (0, 0)

# names = ['Chipotle', 'Cafe Rouge', 'India King']
# contacts = ['Finsbury Sq, Phone : ', 'Park House', 'Pinner']
# categories = [0, 1, 2, 3, 4]

class Rest:
	def __init__(self, idx, food_type, lonlat, name, contacts):
		self.idx_ =  idx
		# self.price_range_ =  price_range
		self.food_type_ = food_type
		self.lonlat_ = lonlat # (ln, lat)
		self.name_ = name
		self.contacts_ = contacts

	def getDistance(self, a, b):
		return math.hypot(b[0] - a[0], b[1] - b[0])

	def getLocation(self):
		return self.lonlat_


	def getData(self, user_location):
		return
		# compute distance and return a feature vector 
		# return [self.price_range_self.getDummy(self.food_type_) + [self.getDistance(user_location, self.lonlat_)]

	def setLocation(self, lonlat):
		self.lonlat_ = lonlat

	def getName(self):
		return self.name_

	def getContacts(self):
		return self.contacts_

	# def getRatings(self, X):
	# 	# compute average rating for the restaurant 
	# 	rest_data = X[:, self.idx_]
	# 	return np.mean(rest_data, axis=0)

	def getDummy(self, val):
		return [1 if val == i else 0 for i in range(5)]

class wrapper:
	def __init__(self):
		self.rests = []
		self.X = None
		
	def getX(self):
		return self.X

	def punchHoles(self, X, num):
		for i in range(num):
			rand_x = randint(0, X.shape[0]-1)
			rand_y = randint(0, X.shape[1]-1)
			X[rand_x, rand_y] = 0
		return X

	def createRestaurants(self):
		restaurants = api.main()

		self.X = np.random.random_integers(0, 5, size=(50., len(restaurants)))
		self.punchHoles(self.X, 20)
		
		# read json files and create resaurants
		for i in range(len(restaurants)):
			self.rests.append(Rest(i, restaurants[i]['categories'], (float(restaurants[i]['location']['coordinate']['longitude']), float(restaurants[i]['location']['coordinate']['latitude'])), str(restaurants[i]['name']), str(restaurants[i]['location']['address'][0])))
		


	def printData(self):
		for i in range(len(self.rests)):
			# print rests[i].getRatings(X)
			print self.rests[i].getContacts()
			print self.rests[i].getName()
			print self.rests[i].getLocation()


	def getReco(self, user):
		rec = rec_sys.getScoresUnvisited(user, self.X)
		unvisited = [(i, elem) for i, elem in enumerate(rec) if elem != -1]
		sorted_rev = sorted(unvisited, key=lambda x: x[1], reverse=True)
		recommendations = []
		for i in range(len(sorted_rev)):
			rest = self.rests[sorted_rev[i][0]]
			recommendations.append([rest.getName(), rest.getLocation()[1], rest.getLocation()[0], i])
		return recommendations





if __name__ == "__main__":
	# a, v = getCommon(a, v)
	# print ncc(a, v)
	createRestaurants()
	printData()
	



# nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(X)
# distances, indices = nbrs.kneighbors(X)


# import knn
# c = knn.wrapper()
# c.createRestaurants()
# c.printData()

