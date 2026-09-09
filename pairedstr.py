strings = input().split()
result = []
left = 0
right = len(strings) - 1
take = 1

while left < right:
	result.append(strings[left][:take])
	result.append(strings[right][-take:])
	left += 1
	right -= 1
	take += 1

print("".join(result))
