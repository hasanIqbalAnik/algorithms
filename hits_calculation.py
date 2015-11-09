import numpy as np

adjacency_mtx = np.matrix([

		[0, 0, 0, 1, 0],
		[0, 0, 0, 1, 1],
		[0, 0, 0, 1, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0]
	])

hub_score = np.matrix([ #initial guess
		[2],
		[2],
		[2],
		[2],
		[2]
	])

authority_score = np.matrix.transpose(adjacency_mtx)*hub_score
hub_score = adjacency_mtx*authority_score


print authority_score
print hub_score