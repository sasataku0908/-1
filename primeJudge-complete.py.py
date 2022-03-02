import time
import math
 
N=input()
N=int(N)
 
start = time.time() 
pattarn=0
for i in range(2, int(math.sqrt(N))):
  if N==2:
    pattarn=1
    break
  elif N % i==0:
    pattarn=1
    break
  else:
    pattarn=0
t = time.time() - start 
#print(t)
if pattarn==1:
  print("No")
elif pattarn==0:
  print("Yes")
