# Stack은 시간 순서상 가장 최근에 추가한 데이터가 가장 먼저 나온다 (후입선출 LIFO[Last In First Out])
# Stack의 top에 데이터를 추가하는 것을 Push
# Stack의 top에 데이터를 추출하는 것을 Pop

stack = []

# append O(1)
stack.append(1) # [1]
stack.append(2) # [1,2]
stack.append(3) # [1,2,3]
stack.append(4) # [1,2,3,4]

# pop O(1)
stack.pop() # [1,2,3]
stack.pop() # [1,2]
stack.pop() # [1]