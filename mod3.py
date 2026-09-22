start=int(input())
end=int(input())
a=[]
for i in range(start, end+1):
  if i%3==0:
    a.append(i)
count=0
for j in a:
  total=0
  while j > 0:
    total += j % 10 
    j //= 10
  if total % 2==0:
    count += 1

print(count)


