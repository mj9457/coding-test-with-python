# Problem: https://leetcode.com/problems/daily-temperatures/

# stack을 활용한 풀이
def DailyTemperatures(temp):
    answer = [0]*len(temp) # 온도를 비교할 변수
    stack = [] # 온도를 비교할 스택

    for cur_day, cur_temp in enumerate(temp): # enumerate를 사용하면 list의 인덱스와 값을 할당, temp의 길이만큼 반복
        while stack and stack[-1][1] < cur_temp: # stack에 원소가 존재하면서 top의 온도가 현재온도보다 낮을때 계속 반복
            prev_day, _ = stack.pop() # stack에 top을 pop으로 빼주고 이전 날짜가 된다
            answer[prev_day] = cur_day - prev_day # answer에서 prev_day가 cur_day부터 기다린 만큼 날짜를 answer에 추가
        stack.append((cur_day,cur_temp)) # stack이 비어있거나 top의 온도가 현재온도보다 높다면 stack의 top에 추가
    return answer

DailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) # [1,1,4,2,1,1,0,0]