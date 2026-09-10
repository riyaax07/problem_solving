print("The matrix is:")
for i in range(R):
  for j in range(C):
    print(mat[i][j],end=" ")
  print()
for i in range(R):
  for j in range(C):
    if i==j:
      print(mat[i][j],end=" ")    
print()