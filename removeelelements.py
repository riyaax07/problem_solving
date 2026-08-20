n=int(input("Enter the number of elements: "))
while n>0:
  a=list(map(int,input("Enter the elements: ").split()))
  del a[a.count(1)]
  print(a)
  n-=1
