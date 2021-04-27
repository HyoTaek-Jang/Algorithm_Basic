'''
과제1-클래스 구조 ver
'''


# Stack 클래스 설정
class Stack():
    def __init__(self, str):
        self.str = str
        self.str_list = list(str)

    def isEmpty(self):
        return len(self.str_list) == 0

    def clear(self):
        self.str_list = []

    def pop(self):
        if not self.isEmpty():
            return self.str_list.pop(-1)

    def __str__(self):
        return str(self.str_list[::-1])

    def clear(self):
        global str_list
        str_list = []

    # palindrome 함수
    def palindrome(self):

        for i in range(len(self.str_list)):
            palindrome_list.append(self.str_list.pop())

        if str_list_copy == palindrome_list:
            return (0)
        else:
            return (1)

        self.str_list.clear()
        palindrome_list.clear()


while True:

    str = input("palindrome을 검사할 문장 입력:")
    if str == "종료":
        print("프로그램을 종료합니다")
        break

    str_list_copy = list(str)
    palindrome_list = []
    a = Stack(str)
    b = a.palindrome()

    if b == 0:
        print("회문구조")
    else:
        print("회문구조가 아닙니다")





