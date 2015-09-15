'''
time complexity of this algorithm: O(m+n) where m and n is the size of two sorted arrays.

idea from: http://articles.leetcode.com/2010/03/here-is-phone-screening-question-from.html
'''

a = [3, 4, 5, 7, 7, 9]
b = [1, 2, 3, 7, 8, 8, 9]
intersect = []

#a intersect b = [3, 7, 9]

la = len(a)
lb = len(b)

ia = 0
ib = 0

while(ia < la and ib < lb):
    if(a[ia] == b[ib]): # a match!
        intersect.append(a[ia])
        ia = ia + 1
        ib = ib + 1
    elif (a[ia] > b[ib]):
        ib = ib + 1
    else:
        ia = ia + 1

print intersect