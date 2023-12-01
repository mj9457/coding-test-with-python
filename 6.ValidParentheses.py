# Problem: https://leetcode.com/problems/valid-parentheses/
# Problem: https://school.programmers.co.kr/learn/courses/30/lessons/12909

# stack을 활용한 풀이
def isValid(s):
    stack = []

    for p in s: # s의 길이만큼 반복한다
        if p == "(": # 여는괄호가 나오면 stack에 닫는괄호를 추가한다
            stack.append(")")
        elif p == "{":
            stack.append("}")
        elif p == "[":
            stack.append("]")
        elif not stack or stack.pop() != p: # stack이 비어있는데 닫는괄호가 나오면 그것은 invalid, top이 p와 다르면 invalid
            return False
    return not stack # stack의 길이가 비어있다면(전부 올바르게 pop 되었다면) True 반환, 하나라도 남는다면 False 반환

isValid(s="()()")  # True
isValid(s="({}[())])") # False