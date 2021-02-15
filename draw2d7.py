#-*- coding: cp932 -*- 
#from visual import * # for vpython6
from vpython import * # for vpython7
import numpy as np

# size of the world (-max <= x <= max and -max <= y <= max)
max=5000.0
canvas(width=1000, height=800,center=vector(0,0,0), background=color.black,resizable=False)

class Point:
    def __init__(self,x=0.0,y=0.0,name=""):
        self.x = x
        self.y = y
        self.name = name
        self.pos = vector(x,y,0)
        self.arr = np.array([x,y])
        self.pic = sphere(pos=self.pos, radius=3,color=color.red)
        self.label = label(pos=self.pos,text=self.name)
        self.pic.visible = False
        self.label.visible = False
    def name(self,name):
        self.name = name
    def draw(self,label=True):
        self.pic.visible = True
        if label and self.name != "": self.label.visible = True
        return
    def hide(self):
        self.pic.visible = False
        self.label.visible = False
        return
    def show(self):
        self.pic.visible = True
        return
    
class Line:
    def __init__(self,p1=Point(0,0),p2=Point(0,0)):
        self.p1 = p1
        self.p2 = p2
        self.pos1 = p1.pos
        self.pos2 = p2.pos
        self.arr1 = p1.arr
        self.arr2 = p2.arr
        self.name = p1.name + p2.name
        self.pic = None
        # [a,b,c] means ax+by=c
        if p1.pos == p2.pos: self.abc = []  # No line
        else:
            (x1,y1) = (p1.x,p1.y)
            (x2,y2) = (p2.x,p2.y)
            if x1 == x2:
                self.abc = [1,0,x1]
            else:
                self.abc = [y1-y2,x2-x1,y1*x2-x1*y2]
        return
    def drawSeg(self,anime=250,color=color.cyan):  # draw the line segment
        v1 = self.pos1
        v2 = self.pos2
        if 0 < anime:
            diff = 500
            mytrail = []
            for t in range(diff):
                rate(anime)
                posDot = v1 + 0.002*t*(v2-v1)
                if t % 20 == 0:
                    dot = sphere(pos=posDot,radius=3,color=color)
                    mytrail.append(dot)
            for i in range(len(mytrail)):
                mytrail[i].visible=False
        pic = curve(pos=[self.pos1,self.pos2],radius=1,color=color)
        self.pic = pic
        return
    def draw(self,anime=250,color=color.cyan):  # draw the line
        p1=self.p1
        p2=self.p2
        v1=self.p1.pos
        v2=self.p2.pos
        if p1 == p2: return
        if p1.x == p2.x:
            v1=vector(p1.x,-max,0)
            v2=vector(p1.x,max,0)
            pic = curve(pos=[v1,v2],radius=1,color=color)
            self.pic = pic
            return
        if p1.y == p2.y:
            v1=vector(-max,p1.y,0)
            v2=vector(max,p1.y,0)
            pic = curve(pos=[v1,v2],radius=1,color=color)
            self.pic = pic
            return
        t1=(1.0*max-p2.x)/(p1.x-p2.x)
        u1=(1.0*max+p2.x)/(p2.x-p1.x)
        t2=(1.0*max-p2.y)/(p1.y-p2.y)
        u2=(1.0*max+p2.y)/(p2.y-p1.y)
        ls=[t1,u1,t2,u2]
        ls.sort()
        tM=ls[1] # minus t
        tP=ls[2] # plus t
        vX=tM*(v1-v2)+v2
        vY=tP*(v1-v2)+v2
        if 0 < anime:
            diff = 500
            mytrail = []
            for t in range(diff):
                rate(anime)
                posDot = v1 + 0.002*t*(v2-v1)
                if t % 20 == 0:
                    dot = sphere(pos=posDot,radius=3,color=color)
                    mytrail.append(dot)
            for i in range(len(mytrail)):
                mytrail[i].visible=False
        pic = curve(pos=[vX,vY],radius=0.5,color=color)
        self.pic = pic
        return
    def hide(self):
        self.pic.visible = False
        return
    def show(self):
        self.pic.visible = True
        return
    
class Circle:
    def __init__(self,c=Point(0,0),p=Point(0,0)):
        self.c = c  # center
        self.p = p  # a point on the circle
        self.name = c.name + p.name
        r = np.linalg.norm(p.arr - c.arr)
        self.radius = r
        self.pic = ring(pos=c.pos,radius=r,axis=vector(0,0,1),thickness=1,color=color.cyan)
        self.pic.visible = False
        return
    def draw(self,anime=250,color=color.cyan): # draw the circle (with animation)
        if anime:
            c = self.c.pos
            p = self.p.pos
            r = self.radius
            diff = 500
            ball = sphere(pos=p, radius=0,color=color,make_trail=False)
            ball.make_trail=False
            mytrail = []
            for t in range(diff):
                rate(anime)
                vecC = self.c.arr
                vecP = self.p.arr
                theta = 2*pi*t/diff
                vecPC = vecP-vecC
                rotM = np.matrix(
                    [[cos(theta),-sin(theta)],
                     [sin(theta),cos(theta)]])
                vecQ = np.dot(rotM,vecPC)+vecC
                ball.pos = vector(vecQ[0,0],vecQ[0,1],0)
                if t % 20 == 0:
                    s = sphere(pos=ball.pos,radius=3,color=color)
                    mytrail.append(s)
            for i in range(len(mytrail)):
                mytrail[i].visible=False
        self.pic.color = color
        self.pic.visible = True
        return
    def hide(self):
        self.pic.visible = False
        return
    def show(self):
        self.pic.visible = True
        return

def mkWorld():
    box(pos=vector(0,0,-0.3),width=0.1,height=max*2,length=max*2)
    curve(pos=[vector(-max,0,0),vector(max,0,0)],radius=0.5,color=color.blue)
    curve(pos=[vector(0,-max,0),vector(0,max,0)],radius=0.5,color=color.blue)
    return

# put a point
def point(x,y,name="",draw=True):
    p = Point(x,y,name)
    if draw:
        p.draw()
    return p

# put a line segment between p1 and p2
def lineSeg(p1,p2,anime=250,draw=True,color=color.cyan):
    ln = Line(p1,p2)
    if draw:
        ln.drawSeg(anime,color)
    return ln

# put a line on p1 and p2
def line(p1,p2,anime=250,draw=True,color=color.cyan):
    ln = Line(p1,p2)
    if draw:
        ln.draw(anime,color)
    return ln

# put a circle on p2 with center p1
def circle(p1,p2,anime=250,draw=True,color=color.cyan):
    circ = Circle(p1,p2)
    if draw:
        circ.draw(anime=anime,color=color)
    return circ

# cross point of two lines
# p = crossPointLL(ln1,ln2,"P") means
# p is the cross point of ln1 and ln2 with name "P"
def crossPointLL(ln1,ln2,name="",draw=True):
    if ln1.abc == [] or ln2.abc == []:
        return # ln1 or ln2 is no-line
    [a1,b1,c1] = ln1.abc
    [a2,b2,c2] = ln2.abc
    a1=a1*1.0
    b1=b1*1.0
    c1=c1*1.0
    a2=a2*1.0
    b2=b2*1.0
    c2=c2*1.0
    if b1 == 0 and b2 == 0:
        return # no cross point
    elif b1 == 0:
        (x,y) = (c1,(c2-a2*c1)/b2)
        p = Point(x,y,name)
    elif b2 == 0:
        (x,y) = (c2,(c1-a1*c2)/b1)
        p = Point(x,y,name)
    else:
        det = a1*b2-a2*b1
        (x,y) = ((c1*b2-c2*b1)/det,(a1*c2-c1*a2)/det)
        p = Point(x,y,name)  
    if draw:
        p.draw()
    return p

# Cross-points
# This calculates cross-points of circ and ax+by=c
# name1 and name2 are names of the cross-points
# It returns
# [] if no cross point exists
# [p1] if one cross point exists
# [p1,p2] if two cross points exist
# Note: (p1.x,p1.y) > (p2.x,p2.y) in the lexicographic order
def crossPointABC(a,b,c,objName,circ,name1,name2,draw=True):
    r = circ.radius
    vecC = circ.c.arr
    cx = vecC[0]
    cy = vecC[1]
    a=a*1.0
    b=b*1.0
    c=c*1.0
    if round(b,3) == 0.0:
        x = c/a
        y1 = cy + sqrt(r**2-(x-cx)**2)
        y2 = cy - sqrt(r**2-(x-cx)**2)
        p1 = Point(x,y1,name1)
        p2 = Point(x,y2,name2)
        if draw:
            p1.draw()
            p2.draw()
        return [p1,p2]
    else:
        a = a/b
        c = c/b
        b = 1.0
        aa = a**2
        bb = b**2
        rr = r**2
        p = cx
        q = cy
        pp = p**2
        k1 = aa+bb
        k2 = a*b*q-a*c-p*bb
        k3 = pp*bb-rr*bb+(b*q-c)**2
        discrim = k2**2-k1*k3
        if discrim < 0:
            print("NoCross: " + objName + " and " + "Circ-" + circ.name) 
            return []
        x1 = (-k2+sqrt(discrim))/k1
        x2 = (-k2-sqrt(discrim))/k1
        y1 = -a*x1/b+c
        y2 = -a*x2/b+c
        p1 = Point(x1,y1,name1)
        if draw:
            p1.draw()
        if discrim == 0:
            print("Tangent")
            return [p1]
        p2 = Point(x2,y2,name2)   
        if draw:
            p2.draw()
        return [p1,p2]    

# cross points of a line and a circle 
def crossPointLC(ln,circ,name1,name2,draw=True):
    [a,b,c] = ln.abc # ln is ax+by=c
    a=a*1.0
    b=b*1.0
    c=c*1.0
    return crossPointABC(a,b,c,"Line-"+ln.name,circ,name1,name2,draw=draw)

def crossPointCC(circ1,circ2,name1,name2,draw=True):
    (p1,q1) = (circ1.c.pos.x,circ1.c.pos.y)
    (p2,q2) = (circ2.c.pos.x,circ2.c.pos.y)
    r1 = circ1.radius
    r2 = circ2.radius
    (pp1,pp2) = (p1**2,p2**2)
    (qq1,qq2) = (q1**2,q2**2) 
    (rr1,rr2) = (r1**2,r2**2)
    a = p2-p1
    b = q2-q1
    c = 0.5*(rr1-rr2-pp1-qq1+pp2+qq2)
    return crossPointABC(a,b,c,"Circ-"+circ2.name,circ1,name1,name2,draw=draw)



##############################################
# いくつかのショートカット
##############################################
# 垂直二等分線．返り値は，pA と pB を結ぶ線分の垂直二等分線
def bisectorLine(pA,pB,anime=250,draw=True,color=color.cyan):
    if draw==False:
        anime = 0
    circAB = circle(pA,pB,draw=False)
    circBA = circle(pB,pA,draw=False)
    [pC,pD] = crossPointCC(circAB,circBA,"","",draw=False)
    lnCD = line(pC,pD,anime=anime,draw=draw,color=color)
    return lnCD

# 中点．返り値は，pA と pB の中点
def middlePoint(pA,pB,name,draw=True):
    circAB = circle(pA,pB,draw=False)
    circBA = circle(pB,pA,draw=False)
    [pC,pD] = crossPointCC(circAB,circBA,"","",draw=False)
    lnAB = line(pA,pB,draw=False)
    lnCD = line(pC,pD,draw=False)
    p = crossPointLL(lnAB,lnCD,name,draw=draw)
    return p

# 垂線．返り値は，[点p を通る直線lnの垂線,その垂線の足]
def suisenLinePoint(ln,p,name,anime=250,draw=True,color=color.cyan):
    if draw==False:
        anime = 0
    p1 = ln.p1
    p2 = ln.p2
    circ = circle(p,p1,draw=False)
    pp = crossPointLC(ln,circ,"","",draw=False)
    if len(pp) < 2:
        circ = circle(p,p2,draw=False)
        pp = crossPointLC(ln,circ,"","",draw=False)
    pA = pp[0]
    pB = pp[1]
    lnS = bisectorLine(pA,pB,anime=anime,draw=draw,color=color)
    pS = crossPointLL(lnS,ln,name,draw=draw)
    return [lnS,pS]

# 垂線．返り値は，点p を通る直線lnの垂線
def suisenLine(ln,p,anime=250,draw=True,color=color.cyan):
    if draw==False:
        anime = 0
    q1 = ln.p1
    if (ln.p1.x == p.x and ln.p1.y == p.y):
        q = ln.p2
    else:
        q = ln.p1
    qdouble = Point(p.x+2*(q.x-p.x), p.y+2*(q.y-p.y))
    circ = circle(p,qdouble,draw=False)
    pp = crossPointLC(ln,circ,"","",draw=False)
    #if len(pp) < 2:
     #   pp[0].hide()
     #   circ = circle(p,p2,draw=False)
     #   pp = crossPointLC(ln,circ,"","",draw=False)
    pA = pp[0]
    pB = pp[1]
    lnS = bisectorLine(pA,pB,anime=anime,draw=draw,color=color)
    return lnS

# 平行線．返り値は，「点p を通り直線lnと平行な直線」
def heikoLine(ln,p,anime=250,draw=True,color=color.cyan):
    if draw==False:
        anime = 0
    lnSui = suisenLine(ln,p,draw=False)
    lnHeiko = suisenLine(lnSui,p,anime=anime,draw=draw,color=color)
    return lnHeiko

# 直線上の異なる3点が順番通りかを調べる．p1,p2,p3 が1つの直線上にあることが前提．p2がp1とp3の間にあれば True，そうでなければ False
def checkLineOrder(p1,p2,p3):
    if (p1.x < p2.x and p2.x < p3.x) or (p1.x > p2.x and p2.x > p3.x):
        return True
    elif p1.x == p2.x and p2.x == p3.x and ((p1.y < p2.y and p2.y < p3.y) or (p1.y > p2.y and p2.y > p3.y)):
        return True
    else:
        return False

# 弧の中心点．返り値は，[劣弧の中心点,優弧の中心点]
# まず中心点を2つ得て，どちらの点がどちらの弧の上の点かを判定するのに checkLineOrder を使う
def arcCenterPoint(circ,p1,p2,name1,name2,draw=True):
    ln = line(p1,p2,draw=False)
    [lnA,pA] = suisenLinePoint(ln,circ.c,"",draw=False)
    p1.show()
    p2.show()
    [pX,pY] = crossPointLC(lnA,circ,"","",draw=False)
    if checkLineOrder(circ.c,pA,pX):
        pX.name = name1
        pY.name = name2
        if draw:
            pX.show()
            pY.show()
        return [pX,pY]
    else:
        pY.name = name1
        pX.name = name2
        if draw:
            pY.show()        
            pX.show()
        return [pY,pX]

# 2点間の三等分．返り値は p1 と p2 を3等分する点 [pM1,pM2]. p1-pM1-pM2-p2 の順
def mid3Points(p1,p2,name1,name2,draw=True):
    ln12 = lineSeg(p1,p2,draw=False)
    c1 = circle(p1,p2,draw=False)
    c2 = circle(p2,p1,draw=False)
    [pX,p] = crossPointCC(c1,c2,"X","",draw=False)
    ln1X = line(p1,pX,draw=False)
    circ1 = circle(pX,p1,draw=False)
    [pY1,pY2] = crossPointLC(ln1X,circ1,"Y","",draw=False)
    pY = pY1 if checkLineOrder(p1,pX,pY1) else pY2
    circ2 = circle(pY,pX,draw=False)
    [pZ1,pZ2] = crossPointLC(ln1X,circ2,"Z","",draw=False)
    pZ = pZ1 if checkLineOrder(pX,pY,pZ1) else pZ2
    lnZ2 = lineSeg(pZ,p2,draw=False)
    lnY = heikoLine(lnZ2,pY,draw=False)
    pM2 = crossPointLL(lnY,ln12,name2,draw=draw)
    lnX = heikoLine(lnZ2,pX,draw=False)
    pM1 = crossPointLL(lnX,ln12,name1,draw=draw)
    return [pM1,pM2]
    
###############################################

mkWorld()
pO = Point(0,0,"O")
pO.draw()

pI = Point(1000,0,"I")
lnOI = line(pO,pI)
suisenLine(lnOI,pO,color=color.red)

#pI = Point(200,0,"I")
#pI.draw()
