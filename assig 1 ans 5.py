
import math

for i in range(0, 360, 15):
   j=math.radians(i) 
   a=math.cos(j)
   b=math.sin(j)

print(i,"---",round(b,4),round(a,4))

