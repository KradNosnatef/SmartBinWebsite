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

    def printAll(self):
        text="["
        currentNode=self.head
        while True:
            if currentNode==None:
                break
            text=text+str(currentNode.data)+" "
            currentNode=currentNode.next
        text=text+"]"
        return(text)

class TowerOfHanoi:
    def __init__(self,rank):
        self.columns=[LinkList(),LinkList(),LinkList()]

        for i in range(0,rank):
            diskSize=rank-i
            self.columns[0].insertIntoHead(diskSize)
        
    def printMyself(self):
        text=self.columns[0].printAll()+self.columns[1].printAll()+self.columns[2].printAll()
        print(text)

    def moveFromAtoB(self,columnAIndex,columnBIndex):
        #your code here


myHanoiTower=TowerOfHanoi(10)
myHanoiTower.printMyself()
