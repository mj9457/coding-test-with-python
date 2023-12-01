# Problem: https://school.programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque

def solution(priorities, location):
    # 프로세스의 우선순위와 위치를 튜플로 묶어서 큐에 저장합니다.
    # enumerate를 통해 인덱스와 값을 함께 가져옵니다.
    queue = deque([(v,i) for i,v in enumerate(priorities)])

    answer = 0  # 실행된 프로세스의 수를 저장하는 변수입니다.

    # 큐에 프로세스가 남아있는 동안 반복합니다.
    while len(queue):
        # 큐에서 프로세스를 하나 꺼냅니다.
        item = queue.popleft()

        # 꺼낸 프로세스보다 우선순위가 높은 프로세스가 큐에 남아있는 경우,
        # 꺼낸 프로세스를 다시 큐의 뒤로 보냅니다.
        if queue and max(queue)[0] > item[0]:
            queue.append(item)
        else:
            # 꺼낸 프로세스가 우선순위가 가장 높은 경우, 프로세스를 실행합니다.
            answer += 1

            # 실행된 프로세스의 초기 위치가 우리가 알고 싶은 프로세스의 위치와 같은 경우,
            # 실행 순서를 반환하고 함수를 종료합니다.
            if item[1] == location:
                break

    return print(answer)  # 프로세스의 실행 순서를 반환합니다.

solution(priorities=[2,1,3,2], location=2)
solution(priorities=[1,1,9,1,1,1], location=0)