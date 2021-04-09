#3 lecture, task E
string = "Мама мыла раму мыла мама папа привет"

print(string.lower().split())

res_str = []
for str in string.lower().split():
    if str not in res_str:
        res_str.append(str)

print(' '.join(res_str))