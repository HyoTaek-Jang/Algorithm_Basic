
def COMPUTE_SMALLEST_H(x):
    # 초기값 세팅
    rule_1 = x
    rule_2 = x
    # 1번 조건으로 줄이고
    if (x - 34) > 0:
        rule_1 = COMPUTE_SMALLEST_H(x - 34)
    # 2번 조건으로 줄이고
    if ((x - 11) / 2) > 0:
        rule_2 = COMPUTE_SMALLEST_H((x - 11) / 2)
    # 더 작은거 return
    return min(rule_1, rule_2)


print(COMPUTE_SMALLEST_H(68.001))
