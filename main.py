#Marley Alford
#Further changes I'd like to make: ability to save file, ability to start over

from Graphics import*
import random
from math import*
#import sys

def makeGraph(graphType):
    if graphType in ("bipartite", "Bipartite"):
        makeBipartite()
    elif graphType in ("complete", "Complete"):
        makeComplete()
    elif graphType in ("cycle", "Cycle"):
        makeCycle()
    elif graphType in ("custom", "Custom"):
        makeCustom()
    else:
        print("Sorry, that graph type does not exist.")

def makeBipartite():
    left = input('How many left vertices? ')
    right = input('How many right vertices? ')
    w = Window(500, 500)
    w.setBackground(Color('white'))
    graph = Bipartite(int(left), int(right), w)
    graph.draw()
    
def makeComplete():
    numVert = input('How many vertices? ')
    if int(numVert) < 0:
        numVert = input('Sorry that is not a valid input, please try again ')
    w = Window(500, 500)
    w.setBackground(Color('white'))
    graph = Complete(int(numVert), w)
    graph.draw()
    
def makeCycle():
    numVert = input('How many vertices? ')
    if int(numVert) < 0:
        numVert = input('Sorry that is not a valid input, please try again ')
    w = Window(500, 500)
    w.setBackground(Color('white'))
    graph = Cycle(int(numVert), w)
    graph.draw()
    
def makeCustom():
    w = Window(500, 500)
    w.setBackground(Color('white'))
    graph = Custom(w)
    print("You are now in custom draw mode.\nPress and hold \'d\' to make vertices\nPress and hold \'l\' to make edges\nPress and hold \'e\' and click mouse to erase all last vertices")
    graph.draw()
    
    
    
    
'''GRAPH CLASS'''
class Graph(object):
    def __init__(self,lvertices,rvertices,win):
        self.lvertices=lvertices
        self.rvertices=rvertices
        #self.vdegree=vdegree
        self.win=win
        self.vertices=[]
        '''circles can be colored'''
        self.lcircles=[]
        self.rcircles=[]
        
    def divideGraph(self):
        '''Divides the graph so that vertices will be evenly spaced, and assigns coordinates to each vertex'''
        pass

    def draw(self):
        '''makes circles out of vertices and connects them by edges according to vdegree'''
        pass
        
class Bipartite(Graph):
    def __init__(self, lvertices, rvertices, w):
        Graph.__init__(self, lvertices, rvertices, w)
        self.lvertices = lvertices
        self.rvertices = rvertices
        #self.vdegree = vdegree
        self.w = w
        self.midway = self.w.getWidth()/2
        self.lbuffer = self.midway-70
        self.rbuffer = self.midway+70
        self.llength = self.w.getHeight()/self.lvertices
        self.rlength = self.w.getHeight()/self.rvertices
        '''a list of vertex points'''
        self.vertices = []
        
    def divideGraph(self):
        pass
        
    def draw(self):
        '''makes the vertices'''
        print("There are", self.lvertices,"left vertices and", self.rvertices, "right vertices.")
        l = self.llength/2
        '''List of lvertex point coordinates'''

        for v in range(self.lvertices):
            p = (self.lbuffer, l)
            self.vertices.append(p)
            c = Circle(p, 5)
            c.draw(self.win)
            self.lcircles.append(c)
            l = l + self.llength

        r = self.rlength/2
        for v in range(self.rvertices):
            p1 = (self.rbuffer, r)
            c = Circle(p1, 5)
            c.draw(self.win)
            self.rcircles.append(c)

            '''makes the connecting edges'''
            for v in range(self.lvertices):
                L1 = (p1)
                L2 = (self.vertices[v])
                l = Line(L1,L2)
                l.draw(self.w)
            r = r + self.rlength



class Complete(Graph):
    def __init__(self, lvertices, w):
        Graph.__init__(self, lvertices, 0, w)
        self.lvertices = lvertices
        self.w = w
        self.vertices = []
        self.circles = []

    def divideGraph(self):
        '''Make a circle that the vertices will appear on'''
        p1 = self.w.getWidth()/2
        p2 = self.w.getHeight()/2
        print(p1, p2)

        #Divide the diameter up into parts
        divided = (2*(150*(pi))) / self.lvertices

        print("Number of vertices is ", self.lvertices)
        
        if self.lvertices == 1:  #if there's only one point, put it in the middle
            P = (p1, p2)
            self.vertices.append((P))
        else:
            for v in range(self.lvertices):
                '''assign coordinate points to each divided part.'''
                p3 = (150*cos((v+1)*((2*pi) / self.lvertices)) + p1)
                p4 = (150*sin((v+1)*((2*pi) / self.lvertices)) + p2)
                P = (p3, p4)
                self.vertices.append((P))
        print(self.vertices)

    def draw(self):
        '''Makes Dots'''
        self.divideGraph()
        for v in self.vertices:
            c = Circle(v,5)
            c.draw(self.w)

        '''Makes edges'''
        L = len(self.vertices)
        for v in range(L):
            p1 = self.vertices[v]
            for v in range(L-1):
                p2 = self.vertices[v+1]
                l = Line(p1, p2)
                l.draw(self.w)

class Cycle(Complete):
    def __init__(self, lvertices, w):
        Complete.__init__(self, lvertices, w)
        self.lvertices = self.lvertices
        self.w = w
        self.vertices = []
        self.circles = []

    def draw(self):
        '''Makes Dots'''
        self.divideGraph()
        for v in self.vertices:
            c = Circle(v,5)
            c.draw(self.w)

        '''Makes edges'''
        L = len(self.vertices)
        for v in range(L):
            if v+1 == L:
                p1 = self.vertices[v]
                p2 = self.vertices[0]
            else:
                p1 = self.vertices[v]
                p2 = self.vertices[v+1]
            l = Line(p1,p2)
            l.draw(self.w)

class Custom(Graph):
    def __init__(self, w):
        Graph.__init__(self, 0, 0, w)
        self.w = w
        self.vertices = []
        self.circles = []           

    def draw(self):
        '''take points made in divideGraph() and turns them into vertices
        c.draw(self.w)'''
        
        while True:
            if self.w.getKeyPressed("d") == True:
                print("Draw mode.")
                n = Point(self.w.getMouse())
                self.vertices.append(n)
                c = Circle(n,5)
                c.draw(self.w)
                self.circles.append(c)
                
            elif self.w.getKeyPressed("e") == True:
                '''deletes all last points created'''
                print("Deleting")
                if self.w.getMouseState() == 'down':
                    if len(self.circles)>0:
                        c = self.circles.pop()
                        v = self.vertices.pop()
                        c.undraw()
                        print("Canvas cleared.")
                        
            elif self.w.getKeyPressed("Escape") == True:
                '''Remember to click activate this.'''
                print("Stopping draw mode.")
                break
                
            elif self.w.getKeyPressed("l") == True:
                print("Line mode.")
                n = self.w.getMouse()
                print("Point chosen.")
                m = self.w.getMouse()
                print("Second point chosen.")
                p1 = n
                p2 = m
                l = Line(p1, p2)
                l.draw(self.w)
                       
        print(self.vertices)
        
    def randGraph(self):
        print("Generating random graph.")
        '''Generates a random set of edges from each of these vertices.'''
        for v in range(len(self.vertices)):
            p1 = self.vertices[v]
            p2 = random.choice(self.vertices)
            l = Line(p1,p2)
            l.draw(self.w)
            
#Initial user prompt
drawMe = raw_input('What type of graph would you like to generate?\n(bipartite, complete, cycle, or custom)')
makeGraph(drawMe)
 
