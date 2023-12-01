class Node:
    # 노드는 값과 다음 값의 주소를 가지고 있다.
    def __init__(self, value=0, nextAddress=None):
        self.value = value
        self.nextAddress = nextAddress


## 시간복잡도 O(n)
class LinkedList(object):
    # head는 None 값을 가리켜야함
    # head는 첫번째 노드값을 가리켜야함

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value): #insert_back
        # n번째 노드는 n+1번째 노드를 가리켜야함
        # 가장 마지막 노드에서 새로운 노드를 추가
        
        newNode = Node(value)

        if self.head is None:
            self.head = newNode # head는 첫번째 노드 고정
            self.tail = newNode # tail은 첫번째 노드에서 시작

            # 위 코드와 동일하게 작동 (연속 할당)
            # self.head = self.tail = newNode 
        else:
            # 시간복잡도 O(n) head만 사용
            current = self.head # current는 head가 가리키는 첫번째 노드 가리킴
            while(current.nextAddress): # 마지막 노드의 nextAddress가 None이 될때 까지 반복
                current = current.nextAddress # current는 다음 주소를 가리키며 마지막 노드까지 이동
            current.nextAddress = newNode # 마지막 노드는 새로운 노드를 가리켜야함

            # 시간복잡도 O(1) head와 tail을 사용
            self.tail.nextAddress = newNode
            self.tail = self.tail.nextAddress
            
    def get(self, index):
        current = self.head # currnet는 head가 가리키는 첫번째 노드부터 시작
        for _ in range(index): # 찾으려하는 index까지 반복
            current = current.nextAddress # current를 다음 주소를 가리키며 index까지 이동
        return current.value # index까지 반복된 current의 value return

    def insert(self, index, value):
        newNode = Node(value)
        current = self.head

        if index == 0: # 첫번째에 넣어야하면
            newNode.nextAddress = self.head # 새로운 노드의 다음주소를 현재 head값을 가리키고
            self.head = newNode # head를 새로운 노드로 바꾼다
        else:
            for _ in range(index-1): # 삽입하는 index 전까지 반복해서
                current = current.nextAddress # current를 이동한다
            newNode.nextAddress = current.nextAddress # 새로운 노드의 다음 주소를 current의 다음 주소를 삽입하고
            current.nextAddress = newNode # current의 다음 주소를 새로운 노드로 삽입한다

    def delete(self, index):        
        current = self.head

        if index == 0: # 첫번째 index라면
            self.head = self.head.nextAddress # head를 head에 다음으로 옮긴다
            # 이렇게되면 garbage callector가 참조하지 않는 메모리를 삭제한다
        else:
            # 제거하려는 노드에 앞 노드를 index가 가리키는 node의 nextAddress로 대체한다
            for _ in range(index-1):
                current = current.nextAddress 
            current.nextAddress = current.nextAddress.nextAddress
            #이렇게되면 garbage callector가 참조하지 않는 메모리를 삭제한다


ll = LinkedList() 
ll.append(11) # 11
ll.append(22) # 11 22
ll.append(33) # 11 22 33
ll.append(44) # 11 22 33 44
ll.insert(index=2, value=99) # 11 22 99 33 44
ll.insert(index=0, value=55) # 55 11 22 99 33 44
ll.insert(index=3, value=77) # 55 11 22 77 99 33 44
ll.delete(index=0) # 11 22 77 99 33 44
ll.delete(index=4) # 11 22 77 99 44

ll.get(0)
ll.get(1)
ll.get(2)
ll.get(3)
ll.get(4)
ll.get(5)