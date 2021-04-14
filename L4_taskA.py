def average(*args):
    sum = 0
    count = 0
    for i in args:
        if int(i) != 0:
            sum += int(i)
            count += 1
    if sum % count == 0:
        return int(sum/count)
    else:
        return sum/count


s = input().split(' ')
list = list(map(int, s))
print(average(*list))
