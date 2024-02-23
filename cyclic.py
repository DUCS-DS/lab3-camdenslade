from llist import *

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

    def createCycle(lst):
        current = lst.head
        count = 1
        cycle_start = None
        while current:
            if count == 10:
                cycle_start = current
            if count == 6:
                cycle_end = current
            current = current.next
            count += 1
        cycle_end.next = cycle_start

    def llprint(lst):
        current = lst.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("...")  


    def findCycle(lst):
        visited = set()
        current = lst.head
        index = 0
        start_index = None
        cycle_length = None

        while current:
            if current in visited:
                if start_index is None:
                    start_index = index
                else:
                    cycle_length = index - start_index
                    break
            else:
                visited.add(current)
            current = current.next
            index += 1
        return start_index, cycle_length



if __name__ == "__main__":
    cyclic_list = LinkedList()
    for i in [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 1024, 2048, 4096, 8192, 16384]:
        cyclic_list.append(i)

    cyclic_list.createCycle()  
    cyclic_list.llprint()  
    cyclic_list.findCycle()
