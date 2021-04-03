# Linked List example

# the Node class

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def get_data(self):
        return self.val

    def set_data(self, new_val):
        self.val = new_val

    def get_next(self):
        return self.next

    def set_next(self, new_node):
        self.next = new_node


# the LinkedList class
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.count = 0

    def get_count(self):
        return self.count

    def insert(self, data):
        new_node=Node(data)
        new_node.set_next(self.head)
        self.head=new_node
        self.count += 1

    def find(self, val):
        item=self.head
        while(item != None):
            if item.get_data() == val:
                return item
            else:
                item=item.get_next()

        return None

    def delete_at(self, index):
        if index > self.count - 1:
            return
        if index == 0:
            self.head = self.head.get_next()
        else:
            tmp = 0
            node = self.head
            while tmp < index -1:
                node = node.get_next()
                tmp += 1
            node.set_next(node.get_next().get_next())
            self.count -= 1

    def print_list(self):
        start=self.head
        while start != None:
            print("Node:", start.get_data())
            start = start.get_next()


itemlist=LinkedList()
itemlist.insert(14)
itemlist.insert(32)
itemlist.insert(92)
itemlist.insert(55)
itemlist.insert(76)
itemlist.print_list()

print(itemlist.find(45))
print(itemlist.find(32))

itemlist.delete_at(3)
print("finding item at index position 3: ", itemlist.find(32))
print("Count after deletion: ", itemlist.get_count())
itemlist.print_list()


