class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(7)
node2 = Node(14)
node3 = Node(21)

node1.next =node2
node2.next = node3
node3.next = node1

temp = node1

while temp:
    print(temp.data , end = "-->")
    temp = temp.next

    if temp ==node1:
        break

print ("starting point")