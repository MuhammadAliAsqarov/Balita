class SingleListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


Head = SingleListNode(1)
B = SingleListNode(2)
C = SingleListNode(3)
D = SingleListNode(4)
Head.next = B
B.next = C
C.next = D
curr = Head
while curr:
    print(curr)
    curr = curr.next 