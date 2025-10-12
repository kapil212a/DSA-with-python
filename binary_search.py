

def binary_search(list1 ,item):
    first =0
    last = len(list1)-1
    found = False

    while(first<=last) and (found == False):
        middle = (first+last)//2

        if list1[middle] == item:
            found  = True

            

        else:
            if list1[middle] > item:
                last = middle-1

            if list1[middle] < item:
                first = middle+1
        
    return found


list1 = [2,4,6,8,12]
print(binary_search(list1 ,8))
