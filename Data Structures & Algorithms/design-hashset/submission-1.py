# Brute force - uses array to check weather a key is in the storage
# class MyHashSet:

#     def __init__(self):
#         self.data = []      

#     def add(self, key: int) -> None:
#         if key not in self.data:
#             self.data.append(key)

#     def remove(self, key: int) -> None:
#         if key in self.data:
#             self.data.remove(key)

#     def contains(self, key: int) -> bool:
#         return key in self.data

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None


# class BinarySearchTree:
#     def __init__(self, root: Node):
#         self.root = root

#     def insert(self, node: Node):
#         self.root = self._insert(node, node.data)

#     def _insert(self, node, key):
#         if node is None:
#             return Node(key)
#         if key < node.left:
#             node.left = self._insert(node.left, key)
#         else:
#             node.right = self._insert(node.right, key)

#     def search(self):
#         pass

#     def delete(self):
#         pass



# class MyHashSet:
#     def __init__(self):
              

#     def add(self, key: int) -> None:
        

#     def remove(self, key: int) -> None:
        

#     def contains(self, key: int) -> bool:
        

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class MyHashSet:
    def __init__(self):
        self.root = None

    def add(self, key: int) -> None:
        self.root = self._add(self.root, key)

    def _add(self, node, key):
        if node is None:
            return TreeNode(key)
        if key < node.key:
            node.left = self._add(node.left, key)
        elif key > node.key:
            node.right = self._add(node.right, key)
        # if equal, do nothing
        return node

    def contains(self, key: int) -> bool:
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def remove(self, key: int) -> None:
        self.root = self._remove(self.root, key)

    def _remove(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:  # found the node to delete
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            # two children: get inorder successor
            succ = self._minValueNode(node.right)
            node.key = succ.key
            node.right = self._remove(node.right, succ.key)
        return node

    def _minValueNode(self, node):
        while node.left:
            node = node.left
        return node
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)