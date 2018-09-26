class LinkedList(object):

    class node(object):
        def __init__(self, value, next_node=None):
            self.value = value
            self.next_node = next_node

    def __init__(self, head_node = None, head=None, next=None, prev=None,
                 tail=None, length=0):
        self.head_node = head_node
        self.head = head
        self.next = next
        self.prev = prev
        self.tail = tail
        self.length = length
        self.current = None
        if self.head_node != None:
            self.insert(head_node)

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current:
            tmp = self.current.value
            self.current = self.current.next_node
            return tmp
        else:
            raise StopIteration()

    def __del__(self):
        self.head_node = self.head = self.next = self.prev = \
            self.tail = self.length = self.current = None

    def __str__(self):
        str_list = ""
        node = self.head
        while node != None:
            if node.next_node != None:
                str_list += str(node.value) + " --> "
            else:
                str_list += str(node.value)
            node = node.next_node
        return str_list

    def insert(self, value):
        new_node = self.node(value)
        if self.head == None:
            self.head = self.tail = new_node
            self.length += 1
        else:
            node = self.tail
            self.tail.next_node = new_node
            self.tail = new_node
            self.length += 1

    def delete(self, value):
        if self.head == None:
            return False
        elif self.head.value == self.tail.value == value and self.length == 1:
            self.head = self.tail = None
            self.length = 0
        elif self.tail.value[0] == value:
            node = self.head
            while node != None:
                prev = node
                node = node.next_node
                if node.value[0] == value:
                    prev.next_node = None
                    self.tail = prev
                    self.length -= 1
                    return True
        else:
            node = self.head
            while node.next_node != None:
                prev = node
                node = node.next_node
                if node.value[0] == value:
                    next = node.next_node
                    prev.next_node = next
                    node.next_node = None
                    self.length -= 1
                    return True
        return False

    def has_node(self, value):
        node_found = False
        if self.head == None:
            node_found = False
        elif self.head.value[0] == value:
            node_found = True
        elif self.tail.value[0] == value:
            node_found = True
        else:
            node = self.head
            while node.next_node:
                prev = node
                node = node.next_node
                if node.value[0] == value:
                    node_found = True
        return node_found

    def get_head(self):
        return str(self.head.value[0])

    def get_length(self):
        return self.length