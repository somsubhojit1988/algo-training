def merge_sort(ary, low, high):
    if low < high:
        #print 'merge_sort() => low = ',low,' high = ',high
        mid = (high +low)/2
        merge_sort(ary, low, mid)
        merge_sort(ary, mid+1, high)
        merge(ary,low,mid,high)
    return ary


def merge(ary,low,mid,high):
    #print 'merge() => low = ',low,' mid = ',mid,' high = ',high,' ary:',ary
    i=low
    j=mid+1
    sortA = []
    for k in range(0,high-low+1):
        #print 'k = ',k,'    i = ',i,' j = ',j
        if i>mid :            
            sortA.append(ary[j])
            j+=1
        elif j>high :
            sortA.append(ary[i])
            i+=1
        elif ary[i] > ary[j] :
            sortA.append(ary[j])
            j+=1
        else :
            sortA.append(ary[i])
            i+=1         
    #print 'merge => ',sortA
    i = 0
    while low <= high:
        ary[low] = sortA[i]
        low+=1
        i+=1

ary = [3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]
print ary, ' => ' 
print merge_sort(ary, 0, len(ary)-1)