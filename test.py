def sol():
    str1 = "5"
    str2 = "2 2 2 4 4"

    num = int(str1)
    people = list(map(int, str2.split()))
    people.sort()

    cnt = 0
    check = 0

    while check < num:
        check += people[check]
        if not check < num:
            break
        cnt += 1

    print(cnt)

sol()
