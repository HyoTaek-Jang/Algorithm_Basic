class Stack:
    def __init__(self, size):
        self.stack = []
        self.size = size
        self.current_size = 0

    def push(self, value):
        if self.size == self.current_size:
            raise Exception("스택이 가득찼습니다.")

        self.stack.append(value)
        self.current_size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("스택이 비어있습니다.")

        self.current_size -= 1
        return self.stack[self.current_size]

    def isEmpty(self):
        return self.current_size == 0

    def peek(self):
        if self.isEmpty():
            raise Exception("스택이 비어있습니다.")
        return self.stack[self.current_size-1]

    def show(self):
        print(self.stack[:self.current_size])

stack = Stack(3)
stack.push(5)
stack.push(2)
stack.show()
stack.pop()
stack.show()
stack.pop()
stack.pop()
