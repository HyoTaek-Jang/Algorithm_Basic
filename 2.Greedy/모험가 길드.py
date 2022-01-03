def solution():
    users = list(map(int, input().split()))
    users.sort()

    answer = 0
    party = []
    for user in users:
        party.append(user)
        if max(party) <= len(party):
            answer += 1
            party.clear()

    print(answer)

solution()