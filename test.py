class Stack():
    def __init__(self):
        self.top=[]

    def push(self,item):
        self.top.append(item)

    def peek(self):
        print(self.top[-1])



def eval():
    s = Stack()

    s.push(1234)
    s.peek()

    