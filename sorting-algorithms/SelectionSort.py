def selection_sort(array):
    for i in range(0,len(array)-1):
        idx = i
        for j in range(i,len(array)):
            if array[idx] > array[j]:
                idx =j
        temp = array[i]
        array[i] = array[idx]
        array[idx] = temp        
    return array
 
ary = [7,6,5,4]
print ary,' => '
print selection_sort(ary)

