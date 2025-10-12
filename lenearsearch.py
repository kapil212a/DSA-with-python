list1 = [12,234,3456,45678,90,1000]
item = 1500

def linear_search(list1 , item):
    for i in list1:
        if i== item:
            
            return True
        

    return False

print(linear_search(list1 , item))