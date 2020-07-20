class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head
        self.current_size = 0

    def size(self):
        return self.current_size

    def is_empty(self, ):
        return self.current_size == 0

    def value_at(self, index):
        if not (0 <= index < self.current_size):
            raise IndexError('Index out of bound')

        if not self.head:
            return None
        else:
            current = self.head
            counter = 0
            while current and counter <= index:
                if counter == index:
                    return current.value
                current = current.next
                counter += 1

            return None

    def push_front(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.current_size += 1

    def pop_front(self):
        if not self.head:
            return None
        else:
            value = self.head.value
            self.head = self.head.next

            self.current_size -= 1
            return value

    def push_back(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        self.current_size += 1

    def pop_back(self):

        if not self.head:
            value = self.head.value
        else:
            current = self.head
            while current.next:
                current = current.next
            value = current.value
            current.next = None
        self.current_size -= 1
        return value

    def front(self):
        return self.head.value if self.head else None

    def back(self):
        if not self.head:
            value = self.head.value
        else:
            current = self.head
            while current.next:
                current = current.next
            value = current.value

        return value

    def insert(self, index, value):
        if not (0 <= index < self.current_size):
            raise IndexError('Index out of bound')

        node = Node(value)
        if not self.head:
            self.head = node
        else:
            current = self.head
            counter = 0
            while current and counter < index - 1:
                current = current.next
                counter += 1
            node.next = current.next
            current.next = node
        self.current_size += 1

    def erase(self, index):
        if not (0 <= index < self.current_size):
            raise IndexError('Index out of bound')

        current = self.head
        counter = 0
        while current and counter < index - 1:
            current = current.next
            counter += 1

        current.next = current.next.next
        self.current_size -= 1

    def value_n_from_end(self, n):
        if not (0 <= n < self.current_size):
            raise ValueError('Value out of bound')

        fast, slow = self.head, self.head
        counter = 0
        while counter < n:
            fast = fast.next
            counter += 1

        while fast.next:
            slow = slow.next
            fast = fast.next

        return slow.value

    def reverse(self):
        previous = None
        current = self.head

        while current.next:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = current

    def remove_value(self, value):
        if not self.head:
            return False

        current = self.head
        previous = None
        while current:
            if current.value == value:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                self.current_size -= 1
                return True

            previous = current
            current = current.next

        return False
