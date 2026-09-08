s = input()

letters = "".join([ch for ch in s if ch.isalpha()])
sum = sum([int(ch) ** 2 for ch in s if ch.isdigit()])

if letters:
    if sum % 2 == 0:
        output = letters[1:] + letters[:1]
    else:
        output = letters[-1:] + letters[:-1]
    
    print(output)
