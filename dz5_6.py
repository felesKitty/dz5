import re

hours_sum = {}

with open('text_6.txt') as subjs:
    for line in subjs.readlines():
        hours_sum[re.findall(r'^\w+', line)[0]] = sum(map(int, re.findall(r'\d+', line)))
        print(hours_sum)
