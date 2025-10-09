m = 40
n = 50
x = m/n
print("fraction form of "  , m ,"/" , n)


list1 = [1,2,3,4,5]
list2 = []

for i in list1:
    list2.insert(0,i)
print(list2)

class Fraction:
    def __init__(self , m ,n):
        self.numer = m
        self.deno = n

    def result(self):
        print("fraction:", self.numer, "/", self.deno)
        print("Numerator:" ,self.numer)
        print("Denominator:", self.deno)

obj1 = Fraction(40,50)
obj1.result()