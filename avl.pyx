"""\
Description:
    This provides AVL implementation with extra support for
    editor components.
    It can be used to implement following data structures
    in very high performance:
    - Rope
    - **Orthogonal** interval trees
Author: Taine Zhao(thautwarm)
License: MIT
"""
from libc cimport stdint

ctypedef stdint.uint8_t bool_t
cdef bool_t true_v = 1
cdef bool_t false_v = 0

cdef class Interval:
    cdef public int start
    cdef public int end

    def __cinit__(self, int start, int end):
        self.start = start
        self.end = end
    
    def __eq__(self, Interval x):
        return self.start == x.start and self.end == x.end
    
    def __lt__(self, Interval x):
        if self.start == x.start:
            return self.end < x.end
        
        return self.start < x.start
    
    def __le__(self, Interval x):
        return self == x or self < x

    def __repr__(self):
        return "[" + str(self.start) + "," + str(self.end) + ")"

cdef class Point:
    cdef public int i
    def __cinit__(self, int i):
        self.i = i
    
    def __lt__(self, Interval interval):
        return self.i < interval.start
    
    def __gt__(self, Interval interval):
        return self.i >= interval.end

    def __eq__(self, Interval interval):
        return interval.start <= self.i < interval.end

cdef object _next(list stack, int direction):
    cdef int visited
    cdef _AVLTree tree
    cdef AVLNode node
    while True:
        if len(stack) == 0:
            return None
        visited, tree = stack[-1]
        # visited    | direction
        # No(0)      | <- (-1)
        # No         | /\ (0)
        # Yes(1)     | -> (1)
        # Yes        | /\
        if visited == false_v:
            if direction == -1:
                if tree.root is None:
                    stack.pop()
                    direction = 0
                    continue
                node = tree.root
                tree = node.left
                stack.append((false_v, tree))
                continue
            else:
                # direction == 0
                node = tree.root
                stack[-1] = (true_v, tree)
                # assert node is not None
                return node
        else:
            if direction == 1:
                node = tree.root
                tree = node.right
                stack.append((false_v, tree))
                direction = -1
                continue
            else:
                # direction == 0
                stack.pop()
                direction = 0
            
        
cdef class iterate_avl:
    cdef list stack
    cdef int direction
    def __cinit__(self, list stack, int direction):
        self.stack = stack
        self.direction = direction
        
    def __next__(self):
        e = _next(self.stack, self.direction)
        self.direction = 1
        if e is None:
            raise StopIteration
        return e
        
    def __iter__(self):
        return self

cdef class AVLNode:
    cdef public object key
    cdef public object value
    cdef _AVLTree left
    cdef _AVLTree right

    def __cinit__(self, object key, object value):
        self.key = key
        self.value = value
        self.left = _AVLTree()
        self.right = _AVLTree()

    def set_key(self, v):
        self._key = v

    def __repr__(self):
        return str(self.key) + '=>' + str(self.value)

cdef inline _AVLTree _unwrap(AVLTree tree):
    return tree.tree

cdef class AVLTree:
    cdef _AVLTree tree
    def __cinit__(self):
        self.tree = _AVLTree()
    
    def __getitem__(self, key):
        cdef _AVLTree tree = self.tree
        return query(tree, key)
    
    def __setitem__(self, key, value):
        
        cdef _AVLTree tree = self.tree
        cdef AVLNode node = AVLNode(key, value)
        if insert(tree, node) == false_v:
            raise ValueError("key", key, "intersected with others")

    def __delitem__(self, key):
        cdef _AVLTree tree = self.tree
        self.tree = delete(tree, key)

    def since(self, key):
        stack = query_with_trace(self.tree, key)
        if stack is None:
            return ()
        return iterate_avl(stack, 0)

    def since_bisect(self, key):
        stack = first_intersection_trace(self.tree, key)
        return iterate_avl(stack, 0)

    def rebalance(self):
        rebalance(self.tree)

    def __iter__(self):
        return iterate_avl([(false_v, self.tree)], -1)
    
    
cdef class _AVLTree:
    cdef object root
    cdef int balance
    cdef int height

    def __cinit__(self):
        self.root = None
        self.height = -1
        self.balance = 0
    

cdef inline void swap_node_rels(_AVLTree t1, _AVLTree t2):
    # boths nodes are nonempty
    cdef AVLNode n1, n2
    n1 = t1.root
    n2 = t1.root

    # n1.value, n2.value = n2.value, n1.value
    # n1.key, n2.key = n2.key, n1.key
    n1.left, n2.left = n2.left, n1.left
    n1.right, n2.right = n2.right, n1.right

    t1.root = n2
    t2.root = n1


cdef _AVLTree delete(_AVLTree self, object key):
    cdef AVLNode root, new_root, parent_root
    cdef _AVLTree left, right, parent
    if self.root is None:
        return self
    
    root = self.root
    if root.key == key:
        left = root.left
        right = root.right
        if left.root is None and right.root is None:
            self.root = None
        elif left.root is None:
            self.root = right.root
        elif right.root is None:
            self.root = left.root
        else:
            left = right
            parent = self
            parent_root = root
            new_root = root
            while left.root is not None:
                parent_root = new_root
                new_root = left.root
                parent = left
                left = new_root.left

            # root.key = new_root.key
            # delete(right, root.key)
            if parent_root is root:
                new_root = right.root
                self.root = new_root
                new_root.left = root.left
            else:
                self, parent_root.left = parent_root.left, self

                new_root.right, root.right = right, new_root.right
                
                # new_root.left is Empty
                new_root.left, root.left = root.left, new_root.left

                new_root.right = delete(right, key)
                assert self.root is new_root
        
        rebalance(self)
        return self
    elif key < root.key:
        left = root.left
        root.left = delete(left, key)
    else:
    # elif key > root.key:
        right = root.right
        root.right = delete(right, key)
    
    rebalance(self)
    return self

cdef inline object query(_AVLTree self, object key):
    cdef AVLNode root
    while True:
        if self.root is None:
            return None
        
        root = self.root
        
        if key == root.key:
            return root
        elif key < root.key:
            self = root.left
        else:
        #elif key > root.key:
            self = root.right

cdef bool_t insert(_AVLTree self, AVLNode node):
    cdef AVLNode root
    cdef bool_t no_intersection

    if self.root is None:
        self.root = node
        return true_v
    
    root = self.root
    
    if node.key == root.key:
        node.left = root.left
        node.right = root.right
        self.root = node
        no_intersection = true_v
    elif node.key < root.key:
        no_intersection = insert(root.left, node)
    elif node.key > root.key:
        no_intersection = insert(root.right, node)
    else:
        return false_v
    
    rebalance(self)
    return no_intersection

cdef void rebalance(_AVLTree self):
    cdef AVLNode node
    cdef _AVLTree tree
    update_height(self, false_v)
    update_balance(self, false_v)

    while self.balance < -1 or self.balance > 1:
        if self.balance > 1:
            node = self.root
            tree = node.left
            if tree.balance < 0:
                rotate_left(node.left)
                update_height(self, true_v)
                update_balance(self, true_v)
            rotate_right(self)
            update_height(self, true_v)
            update_balance(self, true_v)
    
        if self.balance < -1:
            node = self.root
            tree = node.right
            if tree.balance > 0:
                rotate_right(node.right)
                update_height(self, true_v)
                update_balance(self, true_v)
            rotate_left(self)
            update_height(self, true_v)
            update_balance(self, true_v)

cdef inline void rotate_right(_AVLTree self):
    cdef AVLNode root = self.root
    cdef AVLNode new_root, new_left_sub
    cdef _AVLTree tmp

    tmp = root.left
    new_root = tmp.root
    
    tmp = new_root.right
    new_left_sub = tmp.root

    self.root = new_root
    tmp = new_root.right
    tmp.root = root

    tmp = root.left
    tmp.root = new_left_sub

cdef inline void rotate_left(_AVLTree self):
    cdef AVLNode root = self.root
    cdef AVLNode new_root, new_right_sub
    cdef _AVLTree tmp
    
    tmp = root.right
    new_root = tmp.root

    tmp = new_root.left
    new_right_sub = tmp.root

    self.root = new_root
    tmp = new_root.left
    tmp.root = root

    tmp = root.right
    tmp.root = new_right_sub

cdef inline void update_balance(_AVLTree self, bool_t recursive):
    cdef AVLNode root
    cdef _AVLTree left, right

    if self.root is None:
        self.balance = 0
        return

    root = self.root

    left = root.left
    right = root.right
    if recursive == true_v:
        update_balance(left, true_v)
        update_balance(right, true_v)
    
    self.balance = left.height - right.height

cdef inline void update_height(_AVLTree self, bool_t recursive):
    cdef AVLNode root
    cdef _AVLTree left, right
    
    if self.root is None:
        self.height = -1
        return    
    
    root = self.root

    left = root.left
    right = root.right

    if recursive == true_v:
        update_height(left, true_v)
        update_height(right, true_v)
    
    self.height = 1 + max(left.height, right.height)

cdef inline list query_with_trace(_AVLTree self, object key):
    cdef AVLNode root
    cdef list stack = []
    while True:
        if self.root is None:
            return None
        
        root = self.root
        if key == root.key:
            stack.append((false_v, self))
            return stack
        elif key < root.key:
            stack.append((false_v, self))
            self = root.left
        else:
        #elif key > root.key:
            stack.append((true_v, self))
            self = root.right

cdef inline list first_intersection_trace(_AVLTree self, object key):
    """This is useful when key is an interval
    """
    cdef AVLNode root
    cdef list stack = []
    while True:
        if self.root is None:
            # no intersection
            return []
        
        root = self.root
        if key < root.key:
            stack.append((false_v, self))
            self = root.left
        elif key > root.key:
            stack.append((true_v, self))
            self = root.right
        else:
            stack.append((false_v, self))
            return stack

cdef class OrthogonalIntervals:
    cdef _AVLTree tree # Interval -> Bool
    def __cinit__(self):
        self.tree = _AVLTree()
        
    def __getitem__(self, key):
        return query(self.tree, Point(key))

    def affect_insert(self, int start, int delta):
        
        cdef AVLNode node
        cdef Interval interval, first
        affected = []

        # find most valid first interval
        maybe_node = query(self.tree, Point(start))
        if maybe_node is not None:        
            node = maybe_node
            first = node.key
            affected.append(first)
            start = first.start
        
        while True:
            maybe_node = query(self.tree, Point(start - 1))
            if maybe_node is None:
                break
            node = maybe_node
            not_error = node.value
            if not_error:
                first = node.key
                start = first.start
                affected.append(first)
                break
            
            first = node.key
            start = first.start
            affected.append(first)
    
        if not affected:
            return None
        
        end = affected[0].end

        stack = first_intersection_trace(self.tree, Point(end))
        following = iter(iterate_avl(stack, 0))

        for node in following:
            interval = node.key
            not_error = node.value
            if not_error:
                affected.append(interval)
                end = interval.end
                break
            affected.append(interval)
            end = interval.end
            
        for node in following:
            interval = node.key
            interval.start += delta
            interval.end += delta
        
        for interval in affected:
            self.tree = delete(self.tree, interval)
        
        return start, end + delta
    
    def affect_delete(self, int start, int delta):
        cdef AVLNode node
        cdef Interval interval
        
        cdef int affected_bound = start + delta
        stack = first_intersection_trace(self.tree, Point(start))
        following = iter(iterate_avl(stack, 0))
        
        node = next(following)
        interval = node.key
        affected = [interval]
        
        start = interval.start
        end = interval.end

        for node in following:
            interval = node.key
            if interval.start >= affected_bound:
                break
            end = interval.end
            affected.append(interval)

        for interval in affected:
            self.tree = delete(self.tree, interval)
        
        stack = first_intersection_trace(self.tree, Point(end))
        following = iter(iterate_avl(stack, 0))
        for node in following:
            interval = node.key

            interval.start -= delta
            interval.end -= delta
        
        return start, end - delta

    def affect_edit(
        self,
        int start,
        int delete_delta,
        int insert_delta
        ):
        cdef AVLNode node
        cdef Interval interval
        
        cdef int affected_bound = start + delete_delta
        cdef int real_delta = insert_delta - delete_delta
        if delete_delta == 0:
            if insert_delta == 0:
                return None
            return self.affect_insert(start, insert_delta)
        elif insert_delta == 0:
            return self.affect_delete(start, delete_delta)
    
        stack = first_intersection_trace(self.tree, Point(start))
        following = iter(iterate_avl(stack, 0))
        
        node = next(following)
        interval = node.key
        affected = [interval]
        
        start = interval.start
        end =  interval.end
        
        for node in following:
            interval = node.key
            if interval.start >= affected_bound:
                break
            end = interval.end
            affected.append(interval)
        
        for interval in affected:
            self.tree = delete(self.tree, interval)
    
        stack = first_intersection_trace(self.tree, Point(end))
        following = iter(iterate_avl(stack, 0))
        
        for node in following:
            interval = node.key
            interval.start += real_delta
            interval.end += real_delta

        
        return start, end + real_delta


    def insert(self, start, end, value):
        assert start < end
        node = AVLNode(Interval(start, end), value)
        if insert(self.tree, node) == false_v:
            raise ValueError("[", start, ',', end, ") intersected with others")

    def delete(self, start, end):
        assert start < end
        key = Interval(start, end)
        self.tree =  delete(self.tree, key)

    def __iter__(self):
        return iterate_avl([(false_v, self.tree)], -1)
