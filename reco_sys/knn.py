
from sklearn.neighbors import NearestNeighbors
import numpy as np

X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])


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





class Rest:
	def __init__(self, idx, price_range, food_type, location, name, contacts):
		self.idx_ =  idx
		self.price_range_ =  price_range
		self.food_type_ = food_type
		self.location_ = location
		self.name_ = name
		self.contacts_ = contacts


	def getData:
		

nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(X)
distances, indices = nbrs.kneighbors(X)


