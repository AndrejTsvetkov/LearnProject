#3 lecture, task C
print("hi")

string = 'xxxxtttсyyaaax'
com_str = ""
count = 1


for index in range(len(string) - 1):
    if count == 1:
        com_str += string[index]

    if string[index] == string[index + 1]:
        count += 1
        if index + 1 == len(string) - 1:
            com_str += str(count)
    else:
        com_str += str(count)
        count = 1
        if index + 1 == len(string) - 1:
            com_str += string[index + 1] + str(count)



print(com_str)