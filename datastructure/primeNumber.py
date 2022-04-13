def is_prime_number(target):
    if target == 1:
        return True
    for number in range(2, int(target ** 0.5) + 1):
        if target % number == 0:
            return False
    return True


print(is_prime_number(8))
