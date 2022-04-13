class Array:
    def __init__(self, size):
        self.size = size
        self.array = [None] * size

    def set_value(self, idx, value):
        if not (0 <= idx < self.size):
            raise Exception("인덱스를 벗어났습니다.")
        self.array[idx] = value

    def get_value(self, idx):
        if not (0 <= idx < self.size):
            raise Exception("인덱스를 벗어났습니다.")
        if self.array[idx] is None:
            raise Exception("값이 존재하지 않습니다.")

        return self.array[idx]

array = Array(5)
array.set_value(1,4)
print(array.get_value(1))
print(array.get_value(0))
