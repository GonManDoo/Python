class Node:
    def __init__(self, data):
        self.data = data        # 값
        self.next = None        # 다음 노드 지정


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)      # Node 의 data 를 전달

    # 헤더부터 탐색해 뒤에 새로운 노드 추가하기
    def append(self, data):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)

    # 모든 노드 값 출력
    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next
