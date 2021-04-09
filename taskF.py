#3 lecture, task F
str = "Кот нос ток сон клад рама вход книга вдох"

s = str.lower().split(" ")
result = []

for word in s:
    set_word = set(word)
    for other_word in s:
        if word != other_word and set_word == set(other_word):
            if [word, other_word] not in result \
                    and [other_word, word] not in result:
                result.append([word, other_word])


for pair in sorted(result):
    print(' '.join(sorted(pair)))
