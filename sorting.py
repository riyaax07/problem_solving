# a=[2,3,4,5,1]
# a.sort() //in the same while sorted is a new list
# print(a)

n= int(input("Enter the number of elements: "))
a=list(map(int,input("Enter the elements: ").split()))
ord=sorted(a)
print("marks of last five students marks are: ",ord[:5])
print("sum of top five students marks are: ",sum(ord[-5:]))
