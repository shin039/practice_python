# coding:UTF-8

import re

regex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
mo    = regex.search("abdc042-333-3333fgef")
print(mo.group(0))
print(mo.group(1))
print(mo.group(2))
print(mo.group(3))
print(mo.group())

first, second, third = mo.groups()
print(first)
print(second)
print(third)

print(regex.findall('111-222-3333, 444-555-6666'))
