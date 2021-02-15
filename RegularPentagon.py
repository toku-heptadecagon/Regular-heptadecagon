from vpython import*
from draw2d7 import*
from toku import*

#Regular Pentagon
circ=circle(pO,pI)
pa=point(1*pI.x,0,"A")
pb=point(1*pI.x,0,"B")
pc=point(-1*pI.x,0,"C")
[S11,S21]=SolX(pa,pb,pc,"S(1,1)","S(2,1)")
print('s(1,1)=(',S11.x,',',S11.y,')')
print('s(2,1)=(',S21.x,',',S21.y,')')
lnBis=bisectorLine(pO,S11)
csA=crossPointLL(lnX,lnBis,"cos(2π/5)")

lnBis2=bisectorLine(pO,S21)
csB=crossPointLL(lnX,lnBis2,"cos(4π/5)")

lnSui=suisenLine(lnX,csA)
[p1,p4]=crossPointLC(lnSui,circ,"p1","p4")
circ1=circle(p1,pI)
[u,p2]=crossPointCC(circ,circ1,"","p2")
circ2=circle(p2,p1)
[v,p3]=crossPointCC(circ,circ2,"","p3")

lnsg1=lineSeg(pI,p1)
lnsg2=lineSeg(p1,p2)
lnsg3=lineSeg(p2,p3)
lnsg4=lineSeg(p3,p4)
lnsg4=lineSeg(p4,pI)

lnBis.hide()
lnSui.hide()
circ1.hide()
circ2.hide()
circ.hide()
