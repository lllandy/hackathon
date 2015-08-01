import numpy as np
from scipy import spatial


a = [16, 1, 16]
v = [16, 0, 16]
#X = np.random.random_integers(0, 10, size=(10.,5.))
# X = np.array([[ 4,  4,  8, 10,  4],
#        [ 3,  6,  3,  2,  0],
#        [ 6,  4,  9,  8,  6],
#        [ 0,  1,  1,  4,  0],
#        [ 3, 10,  5,  8,  1],
#        [10,  8, 10,  3,  6],
#        [ 6,  8,  9,  1,  7],
#        [ 1, 10,  7,  1,  4],
#        [ 0,  9,  4,  7,  2],
#        [ 3,  4,  6,  1,  8]])

# # a = [1]
# v = [1]


X = np.array([[ 5,  3,  4, 4,  0],
       [ 3,  1,  2,  3,  3],
       [ 4,  3,  4,  3,  5],
       [ 3,  3,  1,  5,  4],
       [ 1, 5,  5,  2,  1]])

# a = [1]



def getCommon(a, v):
	# make sure a and v are equal lengths
	selector = [True if a[i] and v[i] else False for i in range(len(a))]
	a_filt = [a[i] for i, elem in enumerate(selector) if elem]
	v_filt = [v[i] for i, elem in enumerate(selector) if elem]
	return a_filt, v_filt

def idx_unvisited(user, mat):
	user_row = mat[user, :].tolist()
	selector = [True if user_row[i] == 0 else False for i in range(len(user_row))]
	return selector





# def ncc(a, v):
# 	# if (np.std(a) * len(a)) > 0 and  np.std(v) > 0:
# 	# 	a = (a - np.mean(a)) / (np.std(a) * len(a))
# 	# 	v = (v - np.mean(v)) /  np.std(v)
# 	return 1 - spatial.distance.cosine(a, v) # cosine 
# 	# return np.correlate(a, v) # corr


# can also be precomputed 
def ncc(rest1, rest2, mat):
	common = getCommon(mat[:, rest1].tolist(), mat[:, rest2].tolist())
	# if (np.std(a) * len(a)) > 0 and  np.std(v) > 0:
	# 	a = (a - np.mean(a)) / (np.std(a) * len(a))
	# 	v = (v - np.mean(v)) /  np.std(v)
	# return 1 - spatial.distance.cosine(a, v) # cosine 
	# return np.correlate(a, v) # corr
	return 1 - spatial.distance.cosine(common[0], common[1])
	#return ncc(common[0], common[1])


def getSimCoeff(visited, rest, mat):
	scores = [ncc(i, rest, mat) if elem else 0 for i, elem in enumerate(visited)]
	# print scores
	return scores


def getScores(rest, user, mat, unvisited):
	if unvisited[rest] == False:
		return -1 # already been to this rest
	visited = [not i for i in unvisited]
	weights = getSimCoeff(visited, rest, mat) # get weighted score  
	user_ratings = mat[user, :].tolist()
	score = np.dot(weights, user_ratings) / np.sum(weights)
	return score




def getScoresUnvisited(user, mat):
	unvisited =  idx_unvisited(user, mat)
	scores = [getScores(i, user, mat, unvisited) for i, elem in enumerate(unvisited)] # -1 means already rated
	return scores 







if __name__ == "__main__":
	# a, v = getCommon(a, v)
	# print ncc(a, v)
	print getScoresUnvisited(3, X)