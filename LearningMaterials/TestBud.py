#import your module
from LeslieToH import *

#set test case invironment
myHanoiTower=TowerOfHanoi(3)

#test
myHanoiTower.printMyself()
# if myHanoiTower.compareColumnHead(0,1) == True:
#     print('0<1')
# else:
#     print('wrong')

myHanoiTower.solutionToToH()
myHanoiTower.printMyself()