import sys

t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    phoneNumbers = []
    for _ in range(n):
        phoneNumbers.append(sys.stdin.readline().strip())
    answer = True
    phoneNumbers.sort()

    for i in range(len(phoneNumbers)-1):
        if phoneNumbers[i+1].startswith(phoneNumbers[i]):
            answer = False
            break
    if answer:
        ans.append("YES")
    else:
        ans.append("NO")

for i in ans:
    print(i)

