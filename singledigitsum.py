n = int(input("Enter N: "))
k = int(input("Enter K: "))
total = n * k
while len(str(total)) > 1:
    total_sum = 0
    while total > 0:
        total_sum += total % 10
        total //= 10    
    total = total_sum 
print(total)
