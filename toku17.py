from vpython import*
from draw2d7 import*
from toku import*

#t^2+t-4=0
p13=point(-4*pI.x,0,"",draw=False)
[S13,S33]=SolX(pI,pI,p13,"S(1,3)","S(3,3)",draw=False)
print('S(1,3)=(',S13.x,',',S13.y,')')
print('S(3,3)=(',S33.x,',',S33.y,')')

#t^2-S(1,3)t-1=0
p22=PtoMX(S13,"-S(1,3)",draw=False)
p23=PtoMX(pI,"-1",draw=False)
[S12,S92]=SolX(pI,p22,p23,"S(1,2)","S(9,2)",draw=False)
print('S(1,2)=(',S12.x,',',S12.y,')')
print('S(9,2)=(',S92.x,',',S92.y,')')

#t^2-S(3,3)t-1=0
p32=PtoMX(S33,"-S(3,3)",draw=False)
[S32,S272]=SolX(pI,p32,p23,"S(3,2)","S(3*9,2)",draw=False)
print('S(3,2)=(',S32.x,',',S32.y,')')
print('S(3*9,2)=(',S272.x,',',S272.y,')')
#t^2-S(1,2)t+S(3,2)=0
p42=PtoMX(S12,"-S(1,2)",draw=False)
[S11,S131]=SolX(pI,p42,S32,"S(1,1)","S(13,1)")
print('S(1,1)=(',S11.x,',',S11.y,')')
print('S(13,1)=(',S131.x,',',S131.y,')')

S131.hide()


