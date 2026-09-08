k=int(input())
str=input()
r=[]
for i in range(0,len(str),2*k):
  chunk1=str[i:i+k]
  r.append(chunk1)

  chunk2 = str[i + k : i + 2 * k]
  r.append(chunk2[::-1])
print(''.join(r))

