def bubble_sort(list1):
    for i in range(len(list1)):
        for j in range(len(list1)-i-1):
            if list1[j] > list1[j+1]:
                list1[j] ,list1[j+1] = list1[j+1] , list1[j]

    return list1

list1 = [12,65,87,97,43,3]
print(bubble_sort(list1))
