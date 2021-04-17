string = "abcc"

def f(string):
    dict = {}
    for i in string:
        if i not in dict:
            dict[i] = string.count(i)
    max_ = max(dict.values())
    min_ = min(dict.values())
    if max_ == min_ or (max_ - min_ == 1 and list(dict.values()).count(max_) == 1):
        return True
    else:
        return False


print(f(string))
