N=input()
N=int(N)
pattarn=0
for i in range(2, N):
  if N==2:
    pattarn=1
    break
  elif N % i==0:
    pattarn=1
    break
  else:
    pattarn=0
    
if pattarn==1:
  print("No")
elif pattarn==0:
  print（ "はい"）
。
＃＃＃＃＃ 4例#######
