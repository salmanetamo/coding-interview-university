class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def __eq__(self, other):
        return self.value == other.value

    def __gt__(self, other):
        return self.value > other.value

    def __lt__(self, other):
        return self.value < other.value


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = TreeNode(value)
        if self.root:
            current = self.root
            while (node > current and current.right_child is not None) or \
                    (node < current and current.left_child is not None):
                if node > current:
                    current = current.right_child
                else:
                    current = current.left_child

            if node > current:
                current.right_child = node
            elif node < current:
                current.left_child = node
            else:
                return False
        else:
            self.root = node

        return True

    def get_node_count(self):
        pass

    def print_values(self):
        pass

    def delete_tree(self):
        pass

    def is_in_tree(self):
        pass

    def get_height(self):
        pass

    def get_min(self):
        pass

    def get_max(self):
        pass

    def is_binary_search_tree(self):
        pass

    def delete_value(self):
        pass

    def get_successor(self):
        pass


bst = BinarySearchTree()