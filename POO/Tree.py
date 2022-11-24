import numpy as np
import copy

class Tree:
    def __init__(self, state=0):
        self.__state = state
    def get_state(self):
        return self.__state
    def set_state(self,value):
        self.__state = value

    def state_tree(self):
        if self.__state == 0:
            return "."
        elif self.__state == 1:
            return "T"
        elif self.__state == 2:
            return "F"
        elif self.__state == 3:
            return "B"

    def update_tree(self,neigh):
        if neigh == True  and self.__state == 1:
            self.set_state(2)
        elif self.__state == 2:
            self.set_state(3)
class Forest:
    def __init__(self,rows,columns,liste,proba):
        self.__rows=rows
        self.__columns = columns
        self.__liste=liste
        self.__p=proba

    def isburing(self,row,column):
            if self.__liste[row][column].get_state()==2:
                return True
            else:
                return False

# for i in range(0,6):
#     l=[]
#     v=np.random.randint(0,4,1)
#     print(v)
#     l.append(copy.deepcopy(v))


a = Tree(0)
b = Tree(1)
c = Tree(2)
d = Tree(0)
e = Tree(3)
f = Tree(1)

#ici on crée un liste de 6 arbres réparties sue 2 lignes et 3 colonnes 3*2


a.set_state(1)
a.update_tree(True)
print(a.get_state())
print(a.state_tree())

l=[[a,b,c], [d,e,f]]


#print(l[1][1].get_state())

fo=Forest(2,3,l,0.3)
print(fo.isburing(0,1))
