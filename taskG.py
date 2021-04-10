#3 lecture, task G
alphabet = {}
str_ = "Попов Василий Вячеславович"
cir = "абвгдеёжзийклмнопрстуфxцчшщыъэюяь"
latcir = ['a', 'b', 'v', 'g', 'd', 'e', 'e', 'zh', 'z', 'i', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't',
           'u', 'f', 'kh', 'ts', 'ch', 'sh', 'shch', 'y', 'ie', 'e', 'iu', 'ia', '']

alphabet[' '] = ' '
for i in range(len(cir)):
    alphabet[cir[i]] = latcir[i]
    alphabet[cir[i].capitalize()] = latcir[i].capitalize()

for i in str_:
    if i in alphabet:
        str_ = str_.replace(i, alphabet[i])

#print(alphabet.keys())
print(str_)