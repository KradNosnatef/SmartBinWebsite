class LinkListNode:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkList:
    def __init__(self):
        self.head=None

    def insertIntoHead(self,data):
        newNode=LinkListNode(data)
        newNode.next=self.head
        self.head=newNode

    def getAll(self):
        currentNode=self.head
        text="["

        while True:
            if currentNode==None:
                break
            text=text+str(currentNode.data)+" "
            currentNode=currentNode.next

        text=text+"]"
        return(text)

class Stack(LinkList):
    def __init__(self):
        LinkList.__init__(self)

    def push(self,data):
        self.insertIntoHead(data)

    def pop(self):
        result=self.head.data
        self.head=self.head.next
        return(result)

class HanoiTower:
    def __init__(self,rank):
        self.rank=rank
        self.stackList=[Stack(),Stack(),Stack()]
        for i in range(0,rank):
            self.stackList[0].push(rank-i)

    def print(self):
        text=self.stackList[0].getAll()+self.stackList[1].getAll()+self.stackList[2].getAll()
        print(text)

        
