str ="Hello 123 ** hello мама"

dict = {}

for symbol in str.lower():
    if symbol.isalpha():
        if symbol not in dict:
            dict[symbol] = 1
        else:
            dict[symbol] += 1

print(dict.keys())
for key in sorted(dict.keys()):
    print(key, dict[key])

