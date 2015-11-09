import numpy as np
from numpy import linalg as LA

A = np.matrix([[1, -1, 0], 
				[-2, 4, -2], 
				[0, -1, 2]])

egvec = np.matrix([[2],[2],[2]]) #initial guess
egval = 0.0

for i in xrange(20): #after 20 iterations, values seems to converge
	egval = LA.norm(A*egvec)
	egvec = (A*egvec)/egval

print egvec, egval

print "To make sure the results are correct"
print A*egvec 
print ""
print egval*egvec