class Array:
    def __init__(self, capacity=16):
        self.current_capacity = capacity
        self.data = [None] * capacity
        self.current_size = 0

    def size(self):
        """Time complexity: O(1)"""
        '''Space complexity: O(1)'''
        return self.current_size

    def capacity(self):
        return self.current_capacity

    def is_empty(self, ):
        """Time complexity: O(1)"""
        '''Space complexity: O(1)'''
        return self.current_size == 0

    def at(self, index):
        """Time complexity: O(1)"""
        '''Space complexity: O(1)'''
        if not (0 <= index < self.current_size):
            raise IndexError('Index out of bound')

        return self.data[index]

    def push(self, item):
        """Time complexity: O(1)"""
        '''Space complexity: O(1)'''
        if self.current_size == self.current_capacity:
            self.resize(self.current_capacity * 2)

        self.data[self.current_size] = item
        self.current_size += 1

    def insert(self, index, item):
        """Time complexity: O(n)"""
        '''Space complexity: O(1)'''
        if not (0 <= index < self.current_size):
            raise IndexError('Index out of bound')

        if self.current_size == self.current_capacity:
            self.resize(self.current_capacity * 2)

        new_data = self.data[:index] + [item] + self.data[index:]
        self.data = new_data
        self.current_size += 1

    def prepend(self, item):
        """Time complexity: O(n)"""
        '''Space complexity: O(1)'''
        self.insert(0, item)

    def pop(self):
        """Time complexity: O(1)"""
        '''Space complexity: O(1)'''
        if not self.data:
            return None
        item = self.data[self.current_size - 1]
        self.data[self.current_size - 1] = None
        self.current_size -= 1
        return item

    def delete(self, index):
        """Time complexity: O(n)"""
        '''Space complexity: O(1)'''
        new_data = self.data[:index] + self.data[index + 1:]
        self.data = new_data
        self.data[self.current_size] = None
        self.current_size -= 1

    def remove(self, item):
        """Time complexity: O(n)"""
        '''Space complexity: O(1)'''
        for index in range(len(self.data)):
            if item == self.data[index]:
                self.delete(index)

    def find(self, item):
        """Time complexity: O(n)"""
        '''Space complexity: O(1)'''
        for index in range(len(self.data)):
            if item == self.data[index]:
                return index

        return -1

    def resize(self, new_capacity):
        """Time complexity: O(n)"""
        '''Space complexity: O(n)'''
        new_data = [None] * new_capacity
        for index in range(len(self.data)):
            new_data[index] = self.data[index]
        self.data = new_data

    def print(self):
        print(self.data)


array = Array()
print('Size: ' + str(array.size()))
print('Capacity: ' + str(array.capacity()))
print('isEmpty: ' + str(array.is_empty()))
# print('At index 2: ' + str(array.at(2)))
# print('At index out of bound: ' + str(array.at(2000)))
print('Pushing item...')
for i in range(10):
    array.push('Red-' + str(i))
print('Size: ' + str(array.size()))
print('Capacity: ' + str(array.capacity()))
print('isEmpty: ' + str(array.is_empty()))
print('At index 0: ' + str(array.at(0)))
print('Inserting item Yellow at index 5...')
array.insert(5, 'Yellow')
print('At index 5: ' + str(array.at(5)))
print('Prepending item Blue...')
array.prepend('Blue')
array.print()
print('Popping...')
print(array.pop())
print('Size: ' + str(array.size()))