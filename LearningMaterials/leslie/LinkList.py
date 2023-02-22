from LinkisNode import *

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