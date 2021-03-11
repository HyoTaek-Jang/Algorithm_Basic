def solution(brown, yellow):
    h = 3
    while True:
        col = (brown - h * 2) / 2
        yel = col * (h - 2)

        if yel == yellow:
            return [(brown + yellow) // h, h]
        h += 1