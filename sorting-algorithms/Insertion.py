def insertion_sort(array):
    for i in range(1,len(array)):
        j = i-1
        x = array[i]
        while j >= 0 and array[j] > x :
            array[j+1] = array[j]
            j -= 1
        print 'i ',i,' j ',j
        array[j+1] = x

    return array

ary = [47, 47, 43, 44, 43, 45, 38, 34, 31, 29, 21, 13, 10, 4, 2]
# [7,6,5,4]
#insertion_sort(ary)
print ary,' => ',insertion_sort(ary) 