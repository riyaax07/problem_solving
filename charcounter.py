str=input()
n=int(input())
m=int(input())
count=0
for i in str:
  if ord(i)>=n and ord(i)<=m:
    count+=1
print(count)
