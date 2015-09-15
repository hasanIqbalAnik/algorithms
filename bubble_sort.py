''' the average and worst case complexity of bubble sort is O(n^2)
'''

arr = [5, 3, 2, 6, 9, 1]
temp = 0

def bubble_sort(arr):
    for i in xrange(len(arr)-1, -1, -1):
        for j in xrange(0, i, 1):
            if(arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
            print "arr now is: ", arr
        print "outer loop steps here.................."


bubble_sort(arr)

print arr


