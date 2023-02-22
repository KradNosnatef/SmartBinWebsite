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

    def pop(self):
        poppednode = self.head
        self.head = self.head.next
        return poppednode.data

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
        moveData = self.columns[columnAIndex].pop()
        self.columns[columnBIndex].insertIntoHead(moveData)

    def movementA(self):
        for i in range(0,3):
            if self.columns[i].head.data == 1:
                self.moveFromAtoB(i, (i+2)%3)
    
    # if columnIndex1 is the column with the smaller disk (can move), return True, 
    # otherwise return False
    def compareColumnHead(self, columnIndex1, columnIndex2):
        if self.columns[columnIndex1].head == None or self.columns[columnIndex1].head.data > self.columns[columnIndex2].head.data:
            return False
        else:
            return True

    def movementB(self):
        columnWithSmallestIndex = 0
        for i in range(0,3):
            if self.columns[i].head.data == 1: 
                columnWithSmallestIndex = i
                break
        column1Index=(columnWithSmallestIndex+1)%3
        column2Index=(columnWithSmallestIndex+2)%3
        if self.compareColumnHead(column1Index, column2Index) == True:
            self.moveFromAtoB(column1Index, column2Index)
        else:
            self.moveFromAtoB(column2Index, column1Index)
                    
            
        
    # 1. find smallest disk
    # 2. find where is 'left'
    # 3. move from A to B 
