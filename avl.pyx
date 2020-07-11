# language_level: 3
from libc cimport stdint

cdef class AVLNode:
    cdef object _key
    cdef object _value
    cdef AVLTree _left
    cdef AVLTree _right

    def __cinit__(self, object key, object value):
        self._key = key
        self._value = value
        self._left = AVLTree()
        self._right = AVLTree()

    def get_value(self):
        return self._value
    
    def get_key(self):
        return self._key

    def set_key(self, v):
        self._key = v
    
    @property
    def left(self):
        return self._left
    
    @property
    def right(self):
        return self._right
    

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, v):
        self._key = v

    @property
    def value(self):
        return self._value
    
cdef class AVLTree:
    cdef object root
    cdef int balance
    cdef int height

    def __cinit__(self):
        self.root = None
        self.height = -1
        self.balance = 0
    
    def __getitem__(AVLTree self, key):
        return self.query(key)
    
    def __setitem__(self, key, value):
        cdef object node = AVLNode(key, value)
        self.insert(node)

    cdef object query(AVLTree self, object key):
        cdef object root
        cdef AVLTree sub
        if self.root is None:
            return None
        root = self.root
        
        if key == root.key:
            return root
        elif key < root.key:
            sub = root.left
            return sub.query(key)
        else:
            sub = root.right
            return sub.query(key)
    
    cdef inline void update_height(AVLTree self, stdint.uint8_t recursive):
        cdef object root
        cdef AVLTree left, right
        
        if self.root is None:
            self.balance = -1
            return    
        
        root = self.root
        left = root.left
        right = root.right
            
        if recursive:
            left.update_height(recursive)
            right.update_height(recursive)
        
        self.height = 1 + max(left.height, right.height)

    cdef void update_balance(AVLTree self, stdint.uint8_t recursive):
        cdef object root
        cdef AVLTree left, right
        
        if self.root is None:
            self.balance = 0
            return

        root = self.root
        left = root.left
        right = root.right

        if recursive:
            left.update_balance(recursive)
            right.update_balance(recursive)
        
        self.balance = left.height - right.height

    cdef void insert(AVLTree self, AVLNode node):
        cdef object root
        if self.root is None:
            self.root = node
            return
        
        root = self.root
        
        if node.key < root.key:
            root.left.insert(node)
        elif node.key < root.key:
            root.right.insert(node)

        self.rebalance()

    cdef void rebalance(AVLTree self):
        cdef object node
        cdef AVLTree left, right
        self.update_height(0)
        self.update_balance(1)

        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                node = self.root
                left = node.left
                if left.balance < 0:
                    left.rotate_left()
                    self.update_height(1)
                    self.update_balance(1)
                self.rotate_right()
                self.update_height(1)
                self.update_balance(1)
        
            if self.balance < -1:
                node = self.root
                right = node.right
                if right.balance > 0:
                    right.rotate_right()
                    self.update_height(1)
                    self.update_balance(1)
                self.rotate_left()
                self.update_height(1)
                self.update_balance(1)
            
    cdef inline void rotate_left(AVLTree self):
        cdef object root = self.root
        cdef object new_root = root.left.root
        cdef object new_left_sub = new_root.right.root

        self.root = new_root
        new_root.right.root = root
        root.left.root = new_left_sub

    cdef inline void rotate_right(AVLTree self):
        cdef object root
        cdef object new_root
        cdef object new_right_sub

        root = self.root
        new_root = root.right.root
        new_right_sub = new_root.left.root

        self.root = new_root
        new_root.left.root = root
        root.right.root = new_right_sub


