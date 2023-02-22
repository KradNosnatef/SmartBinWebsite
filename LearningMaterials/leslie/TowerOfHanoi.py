from LinkList import *

class TowerOfHanoi:
    def __init__(self,rank):
        self.rank = rank
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
            if self.columns[i].head != None:
                if self.columns[i].head.data == 1:
                    if self.rank % 2 ==1:
                        self.moveFromAtoB(i, (i+2)%3)
                        break
                    else:
                        self.moveFromAtoB(i, (i+1)%3)
                        break
    
    # if columnIndex1 is the column with the smaller disk (can move), return True, 
    # otherwise return False
    # 判空 none check before comparing!!
    def compareColumnHead(self, columnIndex1, columnIndex2):
        if self.columns[columnIndex1].head == None:
            return False
        elif self.columns[columnIndex2].head == None:
            return True
        elif self.columns[columnIndex1].head.data > self.columns[columnIndex2].head.data:
            return False
        else:
            return True

    def movementB(self):
        columnWithSmallestIndex = 0
        for i in range(0,3):
            if self.columns[i].head != None:
                if self.columns[i].head.data == 1: 
                    columnWithSmallestIndex = i
                    break
        column1Index=(columnWithSmallestIndex+1)%3
        column2Index=(columnWithSmallestIndex+2)%3
        if self.compareColumnHead(column1Index, column2Index) == True:
            self.moveFromAtoB(column1Index, column2Index)
        else:
            self.moveFromAtoB(column2Index, column1Index)
                    
    def solutionToToH(self):
        self.printMyself()
        while True:
            self.movementA()
            self.printMyself()
            if self.columns[0].head == None and self.columns[1].head == None:
                break
            self.movementB()
            self.printMyself()
            if self.columns[0].head == None and self.columns[1].head == None:
                break
