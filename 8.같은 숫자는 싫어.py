# Problem: https://school.programmers.co.kr/learn/courses/30/lessons/12906

# stack을 활용한 풀이
def solution(arr):
    answer = []
    
    for i in arr: # 모든 arr를 순회 O(n)
        if len(answer) == 0 or answer[-1] != i: # stack이 비어있거나 top과 arr의 원소를 비교해서 다르다면
            answer.append(i) # stack에 추가
    
    return answer

solution(arr=[1,1,3,3,0,1,1]) # [1,3,0,1]

# javascript 풀이
function solution(arr)
{
    return arr.filter((x, i)=> x != arr[i+1]) // arr의 0번째부터 순회해서 현재 원소와 다음원소를 비교하여 다른것만 필터링처리, O(n)
}