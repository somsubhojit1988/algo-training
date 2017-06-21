def quick_sort(ary, low, high):
    # print 'quick_sort() low ',low,' high',high
    def partition(ary,low,high):
        
        pivot = ary[high]
        pIndex = low
        for j in range(low,high+1):
            if ary[j] < pivot:
                temp = ary[pIndex]
                ary[pIndex] = ary[j]                
                ary[j] = temp
                pIndex +=1
        ary[high] = ary[pIndex]
        ary[pIndex]  = pivot
        # print 'partition() low ',low,' high',high,' pIndex ',pIndex
        return pIndex

    if low < high:
        pIndex = partition(ary,low,high)
        quick_sort(ary, low, pIndex-1)
        quick_sort(ary, pIndex+1, high)
    return ary

#ary = [7,4,3,1]
ary = [2, 7, 1, 6, 8, 5, 3 , 4]
print ary,' = > '
print quick_sort(ary, 0, len(ary)-1)
