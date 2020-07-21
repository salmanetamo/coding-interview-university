class QueueWithArray:
    def __init__(self, max_size=16):
        self.queue = list()
        self.max_size = max_size
        self.head = 0
        self.tail = 0

    def enqueue(self, value):
        if self.is_full():
            return ("Queue is full!")
        else:
            self.queue.append(value)
            self.tail = (self.tail + 1) % self.max_size
            return True

    def dequeue(self):
        if self.is_empty():
            return ("Queue is empty!")
        else:
            value = self.queue[self.head]
            self.head = (self.head + 1) % self.max_size
            return value

    def size(self):
        if self.tail >= self.head:
            qSize = self.tail - self.head
        else:
            qSize = self.max_size - (self.head - self.tail)
        return qSize

    def is_empty(self):
        return self.size() == 0

    def is_full(self):
        return self.size() == self.max_size - 1


class QueueWithLinkedList:
    def __init__(self):
        self.items = SinglyLinkedListWithTail()

    def enqueue(self, value):
        self.items.push_back(value)

    def dequeue(self):
        return self.items.pop_front()

    def is_empty(self):
        return self.items.is_empty()

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class SinglyLinkedListWithTail:
    def __init__(self, head=None):
        self.head = head
        self.tail = None
        self.current_size = 0

    def size(self):
        """Time complexity: O(1)"""
        '''Space complexity: O(1)'''
        return self.current_size

    def is_empty(self, ):
        """Time complexity: O(1)"""
        '''Space complexity: O(1)'''
        return self.current_size == 0

    def value_at(self, index):
        """Time complexity: O(n)"""
        '''Space complexity: O(1)'''
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
        """Time complexity: O(1)"""
        '''Space complexity: O(1)'''
        node = Node(value)
        node.next = self.head
        self.head = node
        if not self.tail:
            self.tail = node
        self.current_size += 1

    def pop_front(self):
        """Time complexity: O(1)"""
        '''Space complexity: O(1)'''
        if not self.head:
            return None
        else:
            value = self.head.value
            self.head = self.head.next
            if not self.head:
                self.tail = None
            self.current_size -= 1
            return value

    def push_back(self, value):
        """Time complexity: O(1)"""
        '''Space complexity: O(1)'''
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.current_size += 1

    def pop_back(self):
        """Time complexity: O(1)"""
        '''Space complexity: O(1)'''
        if not self.head:
            value = self.head.value
        else:
            current = self.head
            while current.next:
                current = current.next
            value = current.value
            current.next = None
            self.tail = current
        self.current_size -= 1
        return value

    def front(self):
        """Time complexity: O(1)"""
        '''Space complexity: O(1)'''
        return self.head.value if self.head else None

    def back(self):
        """Time complexity: O(1)"""
        '''Space complexity: O(1)'''
        if not self.tail:
            value = None
        else:
            value = self.tail.value

        return value

    def insert(self, index, value):
        """Time complexity: O(n)"""
        '''Space complexity: O(1)'''
        if not (0 <= index < self.current_size):
            raise IndexError('Index out of bound')

        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            current = self.head
            counter = 0
            while current and counter < index - 1:
                current = current.next
                counter += 1
            node.next = current.next
            current.next = node
            if not node.next:
                self.tail = node
        self.current_size += 1

    def erase(self, index):
        """Time complexity: O(n)"""
        '''Space complexity: O(1)'''
        if not (0 <= index < self.current_size):
            raise IndexError('Index out of bound')

        current = self.head
        counter = 0
        while current and counter < index - 1:
            current = current.next
            counter += 1

        current.next = current.next.next
        if not current.next:
            self.tail = current
        self.current_size -= 1

    def value_n_from_end(self, n):
        """Time complexity: O(n)"""
        '''Space complexity: O(1)'''
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
        """Time complexity: O(1)"""
        '''Space complexity: O(n)'''
        previous = None
        current = self.head

        while current.next:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = current

    def remove_value(self, value):
        """Time complexity: O(n)"""
        '''Space complexity: O(1)'''
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
