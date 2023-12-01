# Queue는 시간 순서상 먼저 저장한 데이터가 먼저 출력(선입선출 : FIFO[First In First Out])
# linkedList로 구현 하자! 시간 복잡도가 O(1) [ArrayList로 구현하면 시간 복잡도가 O(n)]
# Queue에 rear(끝)에 데이터 추가하는 것을 enqueue
# Queue에 front(앞)에 데이터 추가하는 것을 dequeue

from collections import deque

# enqueue() O(1)
queue = deque()
queue.append(1) #deque([1])
queue.append(2) #deque([1,2])
queue.append(3) #deque([1,2,3])
queue.append(4) #deque([1,2,3,4])

# dequeue() O(1)
queue.popleft() #deque([2,3,4])
queue.popleft() #deque([3,4])
queue.popleft() #deque([4])