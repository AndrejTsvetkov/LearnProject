from collections import Counter

n = int(input())
a = [int(i) for i in input().split()]

# dict = {}
# for i in a:
#     if i not in dict:
#         dict[i] = 1
#     else:
#         dict[i] += 1
#
# print(dict)
#
# max_ = max(dict.values())
# max_list = []
# for key, value in dict.items():
#     if value == max_:
#         max_list.append(key)
#
# print(max(max_list))

counter = Counter(a)

result = a[0]
max_count = counter[result]
for number, count in counter.items():
    if count > max_count or (count == max_count and number > result):
        result = number
        max_count = count

print(result)



