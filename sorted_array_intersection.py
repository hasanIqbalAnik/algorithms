'''
time complexity of this algorithm: O(m+n) where m and n is the size of two sorted arrays. it also removes duplicates

idea from: http://art   icles.leetcode.com/2010/03/here-is-phone-screening-question-from.html
'''

a = [1, 1, 2, 2, 3, 4, 5, 7, 7, 9, 10, 10]
b = [1, 1, 2, 2, 3, 7, 8, 8, 9, 10, 10]
intersect = []

#a intersect b = [3, 7, 9]

la = len(a)
lb = len(b)

ia = 0
ib = 0
ic = 0

while(ia < la and ib < lb):
    if(a[ia] == b[ib]): # a match!
        if not intersect:
            intersect.append(a[ia])
        elif(intersect[ic] != a[ia]):
            intersect.append(a[ia])
            ic = ic + 1
        ia = ia + 1
        ib = ib + 1
    elif (a[ia] > b[ib]):
        ib = ib + 1
    else:
        ia = ia + 1

print intersect