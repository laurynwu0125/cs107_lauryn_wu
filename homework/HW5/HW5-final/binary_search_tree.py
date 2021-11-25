
class BSTNode:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.left = None
        self.right = None
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
        if node == None:
            node = BSTNode(key, val)
        else:
            # key should be put to the left of the node
            if key < node.key:
                if node.left == None:
                    node.left = BSTNode(key, val)
                else:
                    self._put(node.left, key, val)
            # key should be put to the right of the node
            elif key > node.key:
                if node.right == None:
                    node.right = BSTNode(key, val)
                else:
                    self._put(node.right, key, val)

            # key is equal to the node's key, so update the val
            else:
                node.val = val

            node.size = self._size(node.left) + self._size(node.right) + 1

        return node


    def _get(self, node, key):
        if node == None:
            raise KeyError("No such node found with key: ", key)
        else:
            # key should to the left of the node
            if key < node.key:
                return self._get(node.left, key)
            # key should to the right of the node
            elif key > node.key:
                return self._get(node.right, key)
            # key is equal to the node's key, so return the val of the current node
            else:
                return node.val


    @staticmethod
    def _size(node):
        return node.size if node else 0

if __name__ == "__main__":
    greektoroman = BSTTable()
    greektoroman.put('Athena',    'Minerva')
    greektoroman.put('Eros',      'Cupid')
    greektoroman.put('Aphrodite', 'Venus')
    print(greektoroman)
    print(greektoroman.get('Eros'))
    print(greektoroman._size(greektoroman._root))
    #print(greektoroman.get('Not in Table'))
