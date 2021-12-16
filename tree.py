class Node:
    def __init__(self, value):
        self._value = value
        self._parent = None
        self._children = []

    @property
    def value(self):
        return self._value

    @property
    def children(self):
        return self._children

    def add_child(self, node):
        if node not in self._children:
            self._children.append(node)
            if node._parent is not self:
                node.parent = self

    def remove_child(self, node):
        if node in self._children:
            self._children.remove(node)
            if node._parent is not None:
                node.parent = None

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        if self._parent is node:
            return
        if self._parent is not None:
            self._parent.remove_child(self)
        self._parent = node
        if node is not None:
            node.add_child(self)

    def breadth_search(self, value):
        if self._value == value:
            return self
        if len(self.children) == 0:
            return None
        for child in self.children:
            res = child.depth_search(value)
            if res is not None:
                return res

    def depth_search(self, value):
        print(self.value)
        if self.value == value:
            return self
        if len(self.children) == 0:
            return None
        left = self.children[0].depth_search(value)
        if left is not None:
            return left
        for child in self.children[1:]:
            right = child.depth_search(value)
        if right is not None:
            return right
# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)
# node5 = Node(5)
# node6 = Node(6)
# node7 = Node(7)
# node1.add_child(node2)
# node1.add_child(node3)
# node2.add_child(node4)
# node2.add_child(node5)
# node3.add_child(node6)
# node3.add_child(node7)
# print(node1.depth_search(70))
