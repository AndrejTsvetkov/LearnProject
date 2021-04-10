#3 lecture, task H

str = "кот арбуз слово завтрак кнопка лес Лоб"
str1 = "45"

str_list = str.split(" ")
dict = {2: "абвг", 3: "дежз", 4: "ийкл", 5: "мноп", 6: "рсту", 7: "фхцч", 8: "шщъы", 9: "ьэюя"}
result = []

for word in str_list:
    flag = True
    for i in range(len(str1)):
        if word.lower()[i] not in dict[int(str1[i])]:
            flag = False
    if flag:
        result.append(word)

print(" ".join(result))