from vpython import*
from draw2d7 import*
from toku import*
from toku17 import*

circOI=circle(pO,pI)
lnBis=bisectorLine(pO,S11,draw=False)
p=crossPointLL(lnX,lnBis,"cos(2π/17)")
lnSui=suisenLine(lnX,p,draw=False)
[p1,p16]=crossPointLC(lnSui,circOI,"p1","p16")

q=pI
p=p1

for i in range(8):
    circ=circle(p,q)
    lineSeg(q,p,color=color.red)
    q=p
    [x,p]=crossPointCC(circOI,circ,"","p")
    circ.hide()
    print('',i+2,'')

for i in range(6):
    circ=circle(p,q)
    lineSeg(q,p,color=color.red)
    q=p
    [p,x]=crossPointCC(circOI,circ,"p","")
    circ.hide()
    print('',i+10,'')

lineSeg(q,p,color=color.red)
lineSeg(p,p16,color=color.red)
lineSeg(p16,pI,color=color.red)

circOI.hide()

