#!/usr/bin/env python
# coding: utf-8

# In[4]:


class Stack:
    def __init__(self):
        self.top = []

    def isEmpty(self):
        return len(self.top) == 0

    def size(self):
        return len(self.top)

    def clear(self):
        self.top = []

    def push(self, item):
        self.top.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)

    def peek(self):
        if not self.isEmpty():
            return self.top[-1]


# In[5]:


def Palindrome(string):
    s = Stack()
    length = len(string)
    if length % 2 == 0:
        for letter in string[:length // 2]:
            s.push(letter)
        for letter in string[length // 2:]:
            item = s.pop()
            if item != letter:
                s.push(item)
    else:
        for letter in string[:length // 2]:
            s.push(letter)
        for letter in string[length // 2 + 1:]:
            item = s.pop()
            print(length // 2 + 1)
            print(letter)
            if item != letter:
                s.push(item)
    if len(s.top) != 0:
        return print('False')
    else:
        return print('True')


# In[6]:


print("회문을 검사할 단어를 입력하시오.")
stack = Stack()
letters = input()
Palindrome(letters)
while letters != '종료':
    print("회문을 검사할 단어를 입력하시오.")
    stack = Stack()
    letters = input()
    Palindrome(letters)

