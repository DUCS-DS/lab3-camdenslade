from llist import LList, Node, append

class Node:
    def __init__(lst, val, nextNode=None):
        lst.val = val
        lst.next = nextNode

class LinkedList:
    def __init__(lst):
        lst.head = None
        lst.tail = None

    def append(lst, val):
        newNode = Node(val)
        if not lst.head:
            lst.head = newNode
            lst.tail = newNode
        else:
            lst.tail.next = newNode
            lst.tail = newNode

    def prepend(lst, value):
        new_node = Node(value)
        if not lst.head:
            lst.head = new_node
            lst.tail = new_node
        else:
            new_node.next = lst.head
            lst.head = new_node

    def length(self, lst=None):
        if lst is None:
            lst = self 
        count = 0
        current = lst.head
        while current is not None:
            count += 1
            current = current.next
        return count
    
    def llprint(lst):
        current = lst.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")


if __name__ == "__main__":
    llist = LinkedList()
    varlst = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    for i in varlst:
        llist.append(i)
    length = llist.length()
    print(length)
    llist.llprint()

    from genfinite import lst
    lst_length = llist.length(lst)
    print(lst_length)


