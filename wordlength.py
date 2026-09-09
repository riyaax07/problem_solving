# cook your dish here
R = int(input())
C = int(input())
print("Enter", R*C, "values one by one:")
mat = [[input() for _ in range(C)] for _ in range(R)]
for row in mat:
	print(len(row[0]), len(row[-1]))

