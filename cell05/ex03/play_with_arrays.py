#!/usr/bin/env python3

ori_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = []

for i in ori_array:
    if i > 5:
        new_num = i + 2
        if new_num not in new_array:
            new_array.append(new_num)

print(ori_array)
print(new_array)