def f(string):
    max_string = ""
    max_len = 0
    cur_string = ""
    cur_len = 0
    i = 0
    while i != len(string):
        if string[i] not in cur_string:
            cur_len += 1
            cur_string += string[i]
            i += 1
        else:
            if cur_len > max_len:
                max_string = cur_string
                max_len = cur_len
            cur_string = ""
            cur_len = 0
            i = string[:i].rfind(string[i]) + 1
    if cur_len > max_len:
        max_string = cur_string
        max_len = cur_len
    return max_string

string1 = "abcdefa"
string2 = "Good morning, Green orb!"
#print(f(string1))
print(f(string2))
#print(f("11122324455"))
