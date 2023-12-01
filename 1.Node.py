class Node:
    def __init__(self, value=0, next = None):
        self.value = value
        self.next = next

f = Node(1)
s = Node(2)
t = Node(3)
f.next = s
s.next = t
f.value = 6
