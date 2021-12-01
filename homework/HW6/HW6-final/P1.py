from enum import Enum

class BSTNode:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.left, self.right = None, None
        self.size = 1

    def __str__(self):
        return f'BSTNode({self.key}, {self.val})' + \
               '\n|\n|-(L)->' + '\n|      '.join(str(self.left ).split('\n')) + \
               '\n|\n|-(R)->' + '\n|      '.join(str(self.right).split('\n'))


class BSTTable:
    def __init__(self):
        self._root = None

    def __str__(self):
        return str(self._root)

    def __len__(self):
        return self._size(self._root)

    def put(self, key, val):
        self._root = self._put(self._root, key, val)

    def get(self, key):
        return self._get(self._root, key)

    def _put(self, node, key, val):
        if not node:
            return BSTNode(key, val)
        if   key < node.key:
            node.left  = self._put(node.left,  key, val)
        elif key > node.key:
            node.right = self._put(node.right, key, val)
        else:
            node.val = val
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def _get(self, node, key):
        if not node:
            raise KeyError(f'key not found: {key}')
        if   key < node.key:
            return self._get(node.left,  key)
        elif key > node.key:
            return self._get(node.right, key)
        else:
            return node.val

    def removeMinHelper(self, node):
        if node.left == None:
            return node.right
        node.left = self._removemin(node.left)
        node.size = 1 + self._size(node.left) + self._size(node.right)

        return node

    def _removemin(self, node):
        if node == None:
            return None
        node = self.removeMinHelper(node)
        return node

    def minNode(self, node):
        if node == None:
            return None
        if node.left == None:
            return node
        self.minNode(node.left)

    def remove(self, key):
        self._root = self._remove(self._root, key)

    def _remove(self, node, key):
        # TODO: Should return a subtree whose root is <node> but without
        #       the node whose key is <key>
        if node == None:
            raise KeyError("key is not in tree")
            return None
        # recursively seasrch the left subtree
        if key < node.key:
            node.left = self._remove(node.left, key)
        # recursively search the right subtree
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:
            # no right or left child
            if node.right == None:
                return node.left
            if node.left == None:
                return node.right
            # replace with successor
            temp = node
            node = self.minNode(temp.right)
            node.right = self._removemin(temp.right)
            node.left = temp.left

        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node


    @staticmethod
    def _size(node):
        return node.size if node else 0

class DFSTraversalTypes(Enum):
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3

class DFSTraversal():
    def __init__(self, tree: BSTTable, traversalType: DFSTraversalTypes):
        # TODO: implement
        self.type = DFSTraversal
        self.tree = tree
        self.node = self.tree._root

    def __iter__(self):
        return self

    def __next__(self):
        if self.node != None:
            curr_node = self.node
            if self.type == DFSTraversalTypes.PREORDER:
                self.preorder(self.tree)
            elif self.type == DFSTraversalTypes.INORDER:
                self.inorder(self.tree)
            else:
                self.postorder(self.tree)
            print("here")
            return curr_node
        else:
            raise StopIteration

    def inorder(self, bst: BSTTable):
        def helper(node):
            if node != None:
                for x in helper(node.left):
                    yield x
                yield node
                for x in helper(node.right):
                    yield x
            else:
                self.node == None
        helper(bst._root)

    def preorder(self, bst: BSTTable):
        def helper(node):
            yield node
            yield from helper(node.left)
            yield from helper(node.right)
        helper(bst._root)

    def postorder(self, bst: BSTTable):
        def helper(node):
            yield from helper(node.left)
            yield from helper(node.right)
            yield node
        helper(bst._root)


if __name__ == "__main__":
    """
    input_array = [(4, 'a'), (9, 'c'), (2, 'f'), (3, 'z'), (11, 'i'), (8, 'r')]
    bst = BSTTable()

    for key, val in input_array:
        bst.put(key, val)
    print(bst)
    traversal = DFSTraversal(bst, DFSTraversalTypes.INORDER)
    for node in traversal:
        print(str(node.key) + ', ' + node.val)
    """
