def solution(skill, skill_trees):
    answer = 0

    for i in skill_trees:
        temp = 0
        temp_bool = True

        for k in i:
            for j in range(len(skill)):
                if k == skill[j] and j > temp:
                    temp_bool = False
                    break
                elif k == skill[j]:
                    temp += 1

        if temp_bool:
            answer += 1

    return answer