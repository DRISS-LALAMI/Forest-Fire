import numpy as np
import copy
import numpy as np
from tkinter import *
import copy
import random
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

    def isburning(self,row,column):
        if self.__liste[row][column].get_state()==2:
            return True
        else:
            return False
    def burning_neigh(self,row,col):
        for r,c in ((row-1,col),(row+1,col),(row,col-1),(row,col+1)):
           if r>=0 and r< len(self.__liste) and c>=0 and c< len(self.__liste[0]):
                #print("the value of r is",r)
                #print("the value of c is",c)
                if self.isburning(r,c)==True:
                    return True
        else:
           return False

    def update_grid(self):
        l1=copy.deepcopy(self.__liste)
        for row in range(0, self.__rows):
            for column in range(0, self.__columns):
                if self.burning_neigh(row,column) ==True:
                    print("row:"+str(row)+"column:"+str(column))
                    self.__liste[row][column].update_tree(True)
        for row in range(0, self.__rows):
            for column in range(0, self.__columns):
                if self.__liste[row][column].get_state()==2:
                    self.__liste[row][column].get_state() == 3
        return self.__liste

    def get_color(self):
        l=[]
        liste_colors=[]
        for val in self.__liste:
            for elem in val :
                if elem.get_state()==0:
                    l.append("white")
                elif elem.get_state()==1:
                    l.append("green")
                elif elem.get_state()==2:
                    l.append("red")
                elif elem.get_state()==3:
                    l.append("black")
            liste_colors.append(l)
            l=[]
        return liste_colors
    # def set_color(self):
    #     list_colors=[]
    #     l = []
    #     for i in range (0,len(self.__liste)) :
    #         for j in range (len(self.__liste[0])):
    #             v=random.random()
    #             print(v)
    #             print(i)
    #             print(j)
    #             if v<=self.__p:
    #                 l.append("green")
    #             else:
    #                 l.append("white")
    #         list_colors.append(l)
    #         l=[]
    #     return list_colors

    def create_grid(self):
        M = np.array(self.__liste)
        colors = self.get_color()
        root = Tk()

        root.geometry("500x500")
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=1)
        root.columnconfigure(2, weight=1)

        root.rowconfigure(0, weight=1)
        root.rowconfigure(1, weight=1)
        root.rowconfigure(2, weight=1)

        for i in range(len(M)):  # Rows
            for j in range(len(M[0])):  # Columns
                b = Label(root, background=colors[i][j])
                b.grid(row=i, column=j, sticky="sewn")

        mainloop()


a = Tree(1)
b = Tree(2)
c = Tree(0)
d = Tree(2)
e = Tree(3)
f = Tree(1)
g = Tree(1)
h = Tree(2)
i = Tree(1)

#ici on crée un liste de 6 arbres réparties sue 2 lignes et 3 colonnes 3*2

# a.set_state(1)
# a.update_tree(True)
# print("the new state of a is",a.get_state())
# print(a.state_tree())

l=[[a,b,c], [d,e,f], [g,h,i]]


#print(l[1][1].get_state())

fo=Forest(len(l),len(l[0]),l,0.6)
print("is this tree burning ?",fo.isburning(0,1))


row=2
col=1
couple=((row-1,col),(row+1,col),(row,col-1),(row,col+1))
print(couple)
print(fo.get_color())
fo.create_grid()
print(fo.burning_neigh(0,0))
fo.update_grid()
print(fo.get_color())
fo.create_grid()