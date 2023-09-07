def Distance(Ax, Ay, Bx, By):
    DA = Ax**2 + Ay**2
    DB = Bx**2 + By**2

    ans = DA
    if ans > DB:
        ans = DB

    return ans

#print(Distance(12, 5, 12, 9))

class Node:
    data = 0
    next = None
    def __init__(self, val):
        self.data = val

def AddTwoNumbers(list1, list2):
    num1 = 0
    num2 = 0

    while list1:
        num1 = num1*10 + list1.data
        list1 = list1.next

        num2 = num2*10 + list2.data
        list2 = list2.next

    num3 = str(num1 + num2)

    list = Node(num3[0])
    current = list.next
    prev = list

    for i in range(1, len(num3)):
        if current:
            current.data = num3[i]
            prev = current
            current = current.next

    printList(list)

def printList(list1):
    while list1:
        print(list1.data)
        list1 = list1.next


node1 = Node(2)
node2 = Node(4)
node3 = Node(3)

node1.next = node2
node2.next=node3

node4 = Node(5)
node5 = Node(6)
node6 = Node(4)

node4.next = node5
node5.next=node6

AddTwoNumbers(node1, node4)
