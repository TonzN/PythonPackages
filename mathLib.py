import math
import numpy as np
from pylab import *
import operator

ops = {
    "+": (operator.add, 1),
    "-": (operator.sub, 1),
    "*": (operator.mul, 2),
    "/": (operator.truediv, 2),
    "(": (None, 4),
    ")": (None, 4),
    "^": (operator.pow, 3)
}

symb = {
    "e": "2.718281828459",
    "p": "3.1415926535897932"
}


def snittVektsfart(funk, x1, x2):
    if x1 == x2:
        print("\n\tx1 og x2 kan ikke være like!!")
        return 0
    y1 = funk(x1)
    y2 = funk(x2)
    print("\ny1: ", y1)
    print("y2: ", y2)
    if not y1 or not y2:
        return "Ikke mulig å få snittvekstfart"

    return (y2-y1)/(x2-x1)

def deriv(funk, x, delta):
    if x == 0:
        print("\n\t Kan ikke derivere 0")
        return False
    return round((funk(x+delta) - funk(x))/(delta),3) 

def derivA(funk, a, delta): #newtons kvotient
    if a == 0:
        print("\n\t Kan ikek derivere 0")
        return False
    return (round((funk(a+delta)-funk(a-delta))/(2*delta),3))

def derivA2(funk, a, newDelta): #newtons symmetriske kvotient
    if a == 0:
        print("\n\t Kan ikek derivere 0")
        return False
    tilnærming = (funk(a+newDelta)-funk(a))/(newDelta)
    return (round(tilnærming,3)), tilnærming

def derivA2G(funk, a, newDelta): #newtons symmetriske kvotient
    tilnærming = (funk(a+newDelta)-funk(a))/(newDelta)
    return (np.round(tilnærming,3)), tilnærming

def graph(funk, x1,x2, x):
    x_verdier = linspace(x1, x2, x)
    y_verdier = funk(x_verdier)
    dy_verdier, _v = derivA2G(x_verdier)

    plot(x_verdier, y_verdier)
    plot(x_verdier, dy_verdier)
    show()

class Stack:
    def __init__(self, inp = []):
        self.data = inp
    
    def Head(self):
        return self.data[len(self.data)-1]

    def Pop(self):
        item = self.data.pop(len(self.data)-1)
        return item
    
    def Push(self, item):
        self.data.append(item)

class Queue:
    def __init__(self, inp = []):
        self.data = inp
    
    def Head(self):
        return self.data[0]

    def Pop(self):
        item = self.data.pop(0)
        return item
    
    def Push(self, item):
        self.data.append(item)
         
def stringToList(inp):
    new = []
    txt = ""
    for i in inp:
        if i.isnumeric() or i == ".":
            txt += i
        else:
            if txt:
                new.append(float(txt) if "." in txt else int(txt))
                txt = ""
            if i in symb:
                new.append(symb[i])
            else:
                new.append(i)
    if txt:
        new.append(float(txt) if "." in txt else int(txt))
    return new

def ShuntingYard(inp):
    def unpackParantheses(stack, queue):
        for i in reversed(list(stack.data)):
            if i == ")":
                stack.Pop()
                unpackParantheses(stack, queue)
            elif i == "(":
                stack.Pop()
                return
            else:
                item = stack.Pop()
                queue.Push(item)

    inp = stringToList(inp)
    stack = Stack()
    queue = Queue()
    for i in inp:
        if i.isnumeric() or isFloat(i):
            queue.Push(i)
        elif i == ")":
            unpackParantheses(stack, queue)
        elif i == "(":
            stack.Push(i)
        elif i in ops:
            if not stack.data:
                stack.Push(i)
            elif ops[i][1] > ops[stack.Head()][1] or stack.Head() == "(":
                stack.Push(i)
            else: 
                queue.Push(stack.Pop())
                stack.Push(i)
        else:
            print(i, "Is not a valid operator/number")
            return
    for i in range(len(stack.data)):
        queue.Push(stack.Pop())
    return queue


def isFloat(x):
    try:
        float(x)
        return True
    except ValueError:
        False

def Calc(inp):
    inp = ShuntingYard(inp)
    if inp == None:
        return
    output = Stack([])
    while True:
        i = inp.Pop()
        if str(i).isnumeric() or isFloat(i):
            output.Push(i)
        else:
            x = output.Pop()
            output.Push(ops[i][0](float(output.Pop()), float(x)))
        if not inp.data:
            return output.data[0]

def vol_Prism(l,b,h):
    return l*b*h

def surf_Prism(l,b,h):
    return 2*(2*(l+b+h))

def area_Circle(r): 
    return (r**2)*3.4

def surf_Circle(r):
    return (2*3.14*r)

def area_Circle(r):
    return 3.14*(r**2)

def surf_Cyllinder(r,h):
    return Calc()

def area_Sphere(r):
    return 4*3.14*(r**2)

def vol_Sphere(r):
    return (4/3)*3.14*(r**3)

class Vector2:
    def __init__(self, x, y):
        self.vector = (x,y)

    def addVector(self, vector2):
        self.vector = (self.vector[0]+vector2.vector[0], self.vector[1]+vector2.vector[1])
    
    def subVector(self, vector2):
        self.vector = (self.vector[0]-vector2.vector[0], self.vector[1]-vector2.vector[1])
    
    def Scalar(self, k):
        self.vector = (k*self.vector[0], k*self.vector[1])
    
    def VectorOfTwoPoints(a, b):
        return (b[0]-a[0], b[1]-a[1])

    def ScalarProduct(a, b):
        return a.vector[0]*b.vector[0] + a.vector[1] * b.vector[1] 
