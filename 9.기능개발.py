# Problem: https://school.programmers.co.kr/learn/courses/30/lessons/42586

# stack을 활용한 풀이
def solution(progresses, speeds):
    answer = []
    time = 0 # 날짜
    count = 0 # 하루에 완료된 progress 개수

    while len(progresses)> 0: # progress가 완료될때 까지 반복
        if (progresses[0] + time*speeds[0]) >= 100: # 첫번째 progress의 진행도가 100이 넘어가면
            progresses.pop(0) # 첫번째 progress는 삭제
            speeds.pop(0) # 첫번째 progress의 speeds도 삭제
            count += 1 # 완료된 progress 개수 1 증가
        else: # 첫번째 progress가 완료되지 못했다면
            if count > 0: # 완료된 progress가 1개라도 있다면
                answer.append(count) # 완성된 날에 개수 증가
                count = 0 # 완료된 progress 개수 초기화
            time += 1 # 하루 증가
    answer.append(count) # 마지막 progress가 완료됬을 때 추가
    return answer


# deque를 활용한 풀이
from collections import deque

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)

    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]  # 하루에 progress에 해당하는 speed만큼 모든 원소에 증가하면서 첫번째 progress가 완료될때 까지 반복, O(n)
        count = 0 # 하루에 완료된 progress 개수 초기화
        while progresses and progresses[0] >= 100: # progress가 유효하면서 첫번째 progress가 완료됬을때
            progresses.popleft() # 첫번째 progress는 삭제
            speeds.popleft() # 첫번째 progress의 speeds도 삭제
            count += 1 # 하루에 완료된 progress 개수 1씩 추가
        if count: # 하루에 끝난 작업이 있다면
            answer.append(count) # 정답에 원소 추가
    return answer

solution(progresses=[93, 30, 55], speeds=[1, 30, 5])

# javascript 풀이

function solution(progresses, speeds) {
    let answer = [];
    let time = 0;
    let count = 0;
    
    while(progresses.length > 0) {
        if(progresses[0] + time*speeds[0] >= 100) {
            progresses.shift()
            speeds.shift()
            count += 1
        } else {
            if(count > 0) {
                answer.push(count)
                count = 0;
            }
            time += 1
        }
    }
    answer.push(count)
    
    return answer;
}