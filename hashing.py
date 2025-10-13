def hash_function(str1 , table_size):
    sum = 0

    for i in str1 :
        sum = sum + ord(i)

    return(sum%table_size)

table_size = 4

str1 = "python"
print(hash_function(str1 ,table_size))


my_list = [[] , [], [], []] 

def add(name):
    index = hash_function(name , table_size)
    my_list[index].append(name)

add("kapil")
add("rohit")
add("deepak")
add("aman")
print(my_list)

def contains(name):
    index = hash_function(name, table_size)
    return (name in my_list[index])

print(contains("deepak"))