s = "The Tower of London was built in the 15th century"

list = s.split(" ")
print(max(list, key = len))