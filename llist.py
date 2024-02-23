class Node:
    def __init__(lst, val, nextNode=None):
        lst.val = val
        lst.next = nextNode

class LList:
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