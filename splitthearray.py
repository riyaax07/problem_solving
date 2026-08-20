n = int(input("Enter the number of elements: "))
elements_input = input(f"Enter elements: ").split()
arr = [int(x) for x in elements_input[:n]]

max_idx = arr.index(max(arr))
min_idx = arr.index(min(arr))

first_idx = min(max_idx, min_idx)
second_idx = max(max_idx, min_idx)

part_one = arr[0:first_idx]
part_two = arr[first_idx + 1:second_idx]
part_three = arr[second_idx + 1:]

print(part_two + part_one + part_three)