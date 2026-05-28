class BinarySearchNode:
    def __init__(self, key: int, val: int, left: Optional[BinarySearchNode] = None, right: Optional[BinarySearchNode] = None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self, node: Optional[BinarySearchNode] = None):
        self.root = node
    
    def insert(self, node: BinarySearchNode, key: int, val: int) -> Optional[BinarySearchNode]:
        if not node:
            return BinarySearchNode(key, val)
        else: 
            if node.key > key:
                node.left = self.insert(node.left, key, val)
            elif node.key < key:
                node.right = self.insert(node.right, key, val)
            else:
                node.key = key
                node.val = val
        return node
    
    def get(self, node: Optional[BinarySearchNode], key: int) -> Optional[BinarySearchNode]:
        if not node:
            return None
        else: 
            if node.key > key:
                return self.get(node.left, key)
            elif node.key < key:
                return self.get(node.right, key)
            else:
                return node
    
    def get_min(self, node: Optional[BinarySearchNode]) -> Optional[BinarySearchNode]:
        if not node or not node.left:
            return node
        return self.get_min(node.left)
    
    def get_max(self, node: Optional[BinarySearchNode]) -> Optional[BinarySearchNode]:
        if not node or not node.right:
            return node
        return self.get_max(node.right)

    def remove(self, node: Optional[BinarySearchNode], key: int) -> Optional[BinarySearchNode]:
        if not node:
            return None

        if key == node.key:
            if not node.right:
                return node.left
            elif not node.left:
                return node.right

            successor = self.get_min(node.right)
            node.key = successor.key
            node.val = successor.val
            node.right = self.remove(node.right, node.key)

        elif key > node.key:
            node.right = self.remove(node.right, key)
        else:
            node.left = self.remove(node.left, key)
        
        return node
    
    def get_inorder_keys(self, node: Optional[BinarySearchNode], res: Optional[List[int]]) -> List[int]:
        if not node:
            return res

        self.get_inorder_keys(node.left, res)
        res.append(node.key)
        self.get_inorder_keys(node.right, res)

        return res

class TreeMap:
    
    def __init__(self):
        self.__bst = BinarySearchTree()
    
    def insert(self, key: int, val: int) -> None:
        self.__bst.root = self.__bst.insert(self.__bst.root, key, val)

    def get(self, key: int) -> int:
        node = self.__bst.get(self.__bst.root, key)
        if not node:
            return -1
        return node.val

    def getMin(self) -> int:
        if not self.__bst.root:
            return -1
        return self.__bst.get_min(self.__bst.root).val

    def getMax(self) -> int:
        if not self.__bst.root:
            return -1
        return self.__bst.get_max(self.__bst.root).val

    def remove(self, key: int) -> None:
        self.__bst.root = self.__bst.remove(self.__bst.root, key)

    def getInorderKeys(self) -> List[int]:
        return self.__bst.get_inorder_keys(self.__bst.root, [])

