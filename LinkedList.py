class Node:
    def __init__(self,data):
        self.data = data
        self.next =None

def getll(head):
    temp = head

    while temp:
        print(temp.data , end ="-->")
        temp = temp.next

    print(None)

node1 = Node("deepak")
node2 = Node("rohit")
node3 = Node("kapil")
node4 = Node("tusar")

node1.next = node2
node2.next = node3
node3.next = node4


getll(node1)