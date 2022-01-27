def solution(progresses, speeds):
    deploy_idx = 0

    answer = []
    while deploy_idx < len(progresses):
        remain = 100 - progresses[deploy_idx]
        append_cnt = remain // speeds[deploy_idx]
        if remain % speeds[deploy_idx] != 0:
            append_cnt += 1

        cur_answer = 0
        check_continue = True
        for idx in range(deploy_idx, len(speeds)):
            progresses[idx] += speeds[idx] * append_cnt
            if progresses[idx] >= 100 and check_continue:
                cur_answer += 1
            else:
                check_continue = False

        answer.append(cur_answer)
        deploy_idx += cur_answer

    return answer