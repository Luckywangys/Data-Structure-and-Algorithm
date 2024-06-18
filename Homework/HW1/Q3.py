"""
Q3
deletes all the vowels,
inserts a character "." before each consonant,
replaces all uppercase consonants with corresponding lowercase ones.
Vowels are letters "A", "O", "Y", "E", "U", "I", and the rest are consonants.

Input
The first line represents input string of Petya's program.
This string only consists of uppercase and lowercase Latin letters and its length is from 1 to 100, inclusive.
Output
Print the resulting string. It is guaranteed that this string is not empty.
"""

# 2200015507 王一粟
s = input()
c = s.lower()
result = ""
for m in c:
    if m not in "yaeiou":
        result += "." + m
print(result)

#思路：先将字符串小写，然后对非元音字母进行顺序相加以及加入“.”
#耗时：20min