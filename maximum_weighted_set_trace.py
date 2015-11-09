def wis(arr):
	if(len(arr) == 0):
		return 0,0
	A = []
	B = {}
	for i in xrange(len(arr)+1):
		A.insert(i, 0)
	A[0] = 0
	A[1] = arr[0]
	B[arr[0]] = [arr[0]]
	for i in xrange(2, len(arr)+1):	
		print arr[i-1]
		A[i] = max(A[i-1], A[i-2]+arr[i-1])
		try:
			if(A[i-2]+arr[i-1] > A[i-1]):
				B[A[i]] = [B[A[i-2]], arr[i-1]]
		except KeyError:
			B[A[i-2]] = 0
			B[A[i]] = [B[A[i-2]], arr[i-1]]
	return A,B

#res, trace = wis([5, 7, 100, -15, 3, 2])
res, trace = wis([2, 5, 2, 1, 4])
if(res != 0): print  res[len(res)-1]
if (trace != 0): print trace