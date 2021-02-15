#-*- coding: cp932 -*- 
from vpython import * # for vpython6
import numpy as np
from draw2d7 import*

lnX=line(pO,pI)
lnX.draw()

lnY=suisenLine(lnX,pO)
lnY.draw()

#任意の点(p1)から描きたい半径の長さ(p2p3)で円を書く
def makeCircle(p1,p2,p3,draw=True):
    if p1.x==p2.x and p2.x==p3.x and p1.x==0:
        lnSui=suisenLine(lnX,pI,draw=False)
        lnHeiko=heikoLine(lnX,p2,draw=False)
        p=crossPointLL(lnSui,lnHeiko,"",draw=False)
        ln=line(p3,p,draw=False)
        lnHeiko1=heikoLine(ln,p2,draw=False)
        q=crossPointLL(lnHeiko1,lnSui,"",draw=False)
        ln1=line(p1,p,draw=False)
        lnHeiko2=heikoLine(ln1,q,draw=False)
        r=crossPointLL(lnHeiko2,lnY,draw=False)
        circ=circle(p1,r,draw=draw)
        return circ
    elif p1.x==p2.x and p2.x==p3.x:
        lnSui=suisenLine(lnX,p1,draw=False)
        p2y=PointY(p2,"",draw=False)
        p3y=PointY(p3,"",draw=False)
        ln=line(p3y,p1,draw=False)
        lnHeiko1=heikoLine(ln,p2y,draw=False)
        p=crossPointLL(lnHeiko1,lnSui,"",draw=False)
        circ=circle(p1,p,draw=draw)
        return circ
    elif p1.y==p2.y and p2.y==p3.y and p1.y==0:
        pIy=XtoY(pI,"",draw=False)
        lnSui=suisenLine(lnY,pIy,draw=False)
        lnHeiko=heikoLine(lnY,p2,draw=False)
        p=crossPointLL(lnSui,lnHeiko,"",draw=False)
        ln=line(p3,p,draw=False)
        lnHeiko1=heikoLine(ln,p2,draw=False)
        q=crossPointLL(lnHeiko1,lnSui,"",draw=False)
        ln1=line(p1,p,draw=False)
        lnHeiko2=heikoLine(ln1,q,draw=False)
        r=crossPointLL(lnHeiko2,lnX,draw=False)
        circ=circle(p1,r,draw=draw)
        return circ
    elif p1.y==p2.y and p2.y==p3.y:
        lnSui=suisenLine(lnY,p1,draw=False)
        p2x=PointX(p2,"",draw=False)
        p3x=PointX(p3,"",draw=False)
        ln=line(p3x,p1,draw=False)
        lnHeiko1=heikoLine(ln,p2x,draw=False)
        p=crossPointLL(lnHeiko1,lnSui,"",draw=False)
        circ=circle(p1,p,draw=draw)
        return circ
    else:
        ln0=line(p2,p3,draw=False)
        lnHeikop1=heikoLine(ln0,p1,draw=False)
        ln1=line(p1,p2,draw=False)
        lnHeikop3=heikoLine(ln1,p3,draw=False)
        p=crossPointLL(lnHeikop1,lnHeikop3,"",draw=False)
        circ=circle(p1,p,draw=draw)
        return circ

#点のx軸の値を取る
def PointX(p1,name,draw=True):
    if p1.y==0:
        a=p1.x
        p1x=point(a,0,name,draw=draw)
        return p1x
    else:
        lnsui=suisenLine(lnX,p1,draw=False)
        p=crossPointLL(lnX,lnsui,name,draw=draw)
        return p

#点のy軸の値を取る
def PointY(p1,name,draw=True):
    if p1.x==0:
        a=p1.y
        p1y=point(o,a,name,draw=draw)
        return p1y
    else:
        lnsui=suisenLine(lnY,p1,draw=False)
        p=crossPointLL(lnY,lnsui,name,draw=draw)
        return p

#x軸の値をy軸に持ってくる
def XtoY(p1,name,draw=True):
    if p1.x<0:
        p1x=PointX(p1,"",draw=False)
        circ=circle(pO,p1x,draw=False)
        [p,q]=crossPointLC(lnY,circ,"",name,draw=draw)
        p.hide()
        return q
    elif p1.y==0:
        circ=circle(pO,p1,draw=False)
        [p,q]=crossPointLC(lnY,circ,name,"",draw=draw)
        q.hide()
        return p
    else:
        p1x=PointX(p1,"",draw=False)
        circ=circle(pO,p1x,draw=False)
        [p,q]=crossPointLC(lnY,circ,name,"",draw=draw)
        q.hide()
        return p

#y軸の値をx軸に持ってくる
def YtoX(p1,name,draw=True):
    if p1.y<0:
        p1y=PointY(p1,"",draw=False)
        circ=circle(pO,p1y,draw=False)
        [p,q]=crossPointLC(lnX,circ,"",name,draw=draw)
        p.hide()
        return q
    elif p1.x==0:
        circ=circle(pO,p1,draw=False)
        [p,q]=crossPointLC(lnX,circ,name,"",draw=draw)
        q.hide()
        return p
    else:
        p1y=PointY(p1,"",draw=False)
        circ=circle(pO,p1y,draw=False)
        [p,q]=crossPointLC(lnX,circ,name,"",draw=draw)
        q.hide()
        return p
    
#a+b,a-b(name1=a+b,name2=a-b)
#x座標の加減
def addX(p1,p2,name1,name2,draw=True):
    p1x=PointX(p1,"",draw=False)
    p2x=PointX(p2,"",draw=False)
    circ=makeCircle(p1x,pO,p2x,draw=False)
    if p1.x<0 and p2.x<0:
        [p,q]=crossPointLC(lnX,circ,name2,name1,draw=draw)
        return [p,q]
    elif p1.x>0 and p2.x<0:
        [p,q]=crossPointLC(lnX,circ,name2,name1,draw=draw)
        return [q,p]#201207見直し必要→201218OK!
    else:
        [p,q]=crossPointLC(lnX,circ,name1,name2,draw=draw)
        return [p,q]#ok

#a*b
#x座標の乗法
def mulX(p1,p2,name,draw=True):
    if p1.x==0 or p2.x==0:
         return pO
    elif p1.y==p2.y and p1.y==0:#201207mul書き換えた要確認→201218OK!
        b=XtoY(p2,"",draw=False)
        pIy=XtoY(pI,"",draw=False)
        ln=line(p1,pIy,draw=False)
        lnHeiko=heikoLine(ln,b,draw=False)
        p=crossPointLL(lnX,lnHeiko,name,draw=draw)
        return p
    else:
        a=PointX(p1,"",draw=False)
        b=XtoY(p2,"",draw=False)
        pIy=XtoY(pI,"",draw=False)
        ln=line(a,pIy,draw=False)
        lnHeiko=heikoLine(ln,b,draw=False)
        p=crossPointLL(lnX,lnHeiko,name,draw=draw)
        return p
    
#a/b
#x座標の除法
def divX(p1,p2,name,draw=True):
    if p2.x==0:
        print("error!")
        return
    elif p1.x==0:
        return pO
    else:
        pIy=XtoY(pI,"",draw=False)
        a=PointX(p1,"",draw=False)
        p2x=PointX(p2,"",draw=False)
        b=XtoY(p2x,"",draw=False)
        ln=line(a,b,draw=False)
        lnHeiko=heikoLine(ln,pIy,draw=False)
        p=crossPointLL(lnX,lnHeiko,name,draw=draw)
        return p

#rootX
def rootX(p1,name,draw=True):
    if p1.x<pI.x:
        print("error!")
        return
    elif p1.x==pI.x and p1.y==0:
        circ=circle(pO,pI,draw=False)
        [a,b]=crossPointLC(lnX,circ,name,"",draw=draw)
        b.hide()
        return a
    elif p1.x==pI.x:
        p1x=PointX(p1,name,draw=draw)
        return p1x        
    else:
        [p,q]=addX(p1,pI,"","",draw=False)#p=a+1,q=a-1
        lnBis1=bisectorLine(pO,p,draw=False)#a+1/2
        lnBis2=bisectorLine(pO,q,draw=False)#a-1/2
        r=crossPointLL(lnBis1,lnX,"",draw=False)#r=a+1/2
        s=crossPointLL(lnBis2,lnX,"",draw=False)#s=a-1/2
        t=XtoY(s,"",draw=False)#t=a-1/2
        w=XtoY(r,"",draw=False)#w=a+1/2
        circ=makeCircle(t,pO,w,draw=False)
        [u,v]=crossPointLC(lnX,circ,name,"",draw=draw)
        v.hide()
        return u

#符号変え
def PtoMX(p1,name,draw=True):
    p1x=PointX(p1,"",draw=False)
    circ=circle(pO,p1x,draw=False)
    if p1x.x>0:
        [x1,p]=crossPointLC(lnX,circ,"",name,draw=draw)
        x1.hide()
        return p
    else:
        [p,x1]=crossPointLC(lnX,circ,name,"",draw=draw)#-b
        x1.hide()
        return p
    
#解の公式
def SolX(pa,pb,pc,name2,name1,draw=True):
    p2=point(2*pI.x,0,"",draw=False)
    p4=point(4*pI.x,0,"",draw=False)
    a=PointX(pa,"",draw=False)
    b=PointX(pb,"",draw=False)
    c=PointX(pc,"",draw=False)
    bb=mulX(b,b,"",draw=False)#b^2
    ac=mulX(a,c,"",draw=False)#a*c
    ac4=mulX(p4,ac,"",draw=False)#4*a*c
    [x1,D]=addX(bb,ac4,"","",draw=False)
    rD=rootX(D,"",draw=False)#√(D)
    mb=PtoMX(b,"",draw=False)#-b    
    [Dpb,Dmb]=addX(mb,rD,"","",draw=False)#-b+√D,-b-√D    
    pa2=mulX(p2,pa,"",draw=False)#2*a    
    ans2=divX(Dmb,pa2,name1,draw=draw)#-b-√D/2a    
    ans1=divX(Dpb,pa2,name2,draw=draw)#-b+√D/2a    
    return [ans1,ans2]
