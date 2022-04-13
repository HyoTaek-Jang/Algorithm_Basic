def count_zero_seven(target):
    target = (list(str(target)))
    count = 0
    for current in target:
        if current == '0' or current == '7':
            count += 1

    return count

print(count_zero_seven(1231237))