R = int(input())
C = int(input())
print("Enter", R*C, "values one by one:")
mat = [[input() for _ in range(C)] for _ in range(R)]
print(mat)