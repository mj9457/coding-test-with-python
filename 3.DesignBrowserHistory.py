# Problem: https://leetcode.com/problems/design-browser-history/

class Node(object):
    def __init__(self, value=0, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class BrowserHistory(object):

    def __init__(self, homepage):
        self.head = self.current = Node(value=homepage) # head와 current는 새롭게 생성된 homepage를 값으로 가지는 Node를 가리킨다

    def visit(self, url):
        self.current.next = Node(value=url, prev=self.current) # current의 다음을 연결하는데 새로운 Node를 생성하고 이 Node의 전 값을 현재값으로 둔다 (새로운 Node 생성)
        self.current = self.current.next # current는 새로 생성된 Node로 이동한다

    def back(self, steps):
        while steps > 0 and self.current.prev: # steps 만큼 (current의 prev값이 None이 아닐때까지) 반복한다
            steps -= 1
            self.current = self.current.prev # current를 prev로 반복 이동
        return self.current.value # 마지막엔 current의 value를 리턴

    def forward(self, steps):
        while steps > 0 and self.current.next: # steps 만큼 (current의 next값이 None이 아닐때까지) 반복한다
            steps -= 1
            self.current = self.current.next # current를 next로 반복 이동
        return self.current.value # 마지막엔 current의 value를 리턴
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)