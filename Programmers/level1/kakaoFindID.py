import re


def solution(new_id):
    # 규칙 1
    new_id = new_id.lower()

    # 규칙 2
    temp = ""
    for i in new_id:
        if i.isalpha() or i.isdigit() or i == '-' or i == '_' or i == '.':
            temp += i

    # 규칙3
    p = re.compile(r'[.]{2,}')
    temp = p.sub('.', temp)

    # 규칙4
    p = re.compile('^[.]|[.]$')
    temp = p.sub('', temp)

    # 규칙5
    if len(temp) == 0:
        temp = 'a'

    # 규칙6
    if len(temp) > 15:
        temp = temp[:15]
    p = re.compile('[.]$')
    temp = p.sub('', temp)

    # 규칙7
    while len(temp) < 3:
        temp += temp[len(temp) - 1]

    return temp

a = solution("...!@BaT#*..y.abcdefghijklm")
print(a)