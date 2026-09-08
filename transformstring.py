a=input()
result=""
for ch in a:
    if ch.isalnum():
        result+=ch.lower()
for ch in a:
    if not ch.isalnum():
        result+=ch
print(result)