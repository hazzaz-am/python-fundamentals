a = range(1, 20, 1)
b = range(1, 5)
c = range(16, 0, -1)


for i in c:
    print(i)

d = "Hazzaz"
dd = ""

for i in range(0, len(d)):
    print(d[i])

for char in d:
    print(char)

print(d[::-1])
for char in range(len(d) - 1, -1, -1):
    dd += d[char]

print(dd)

e = "asd978@#$234"
alpha = 0
digit = 0
special_char = 0

for i in e:
    if i.isalpha():
        alpha += 1
    elif i.isdigit():
        digit += 1
    else :
        special_char += 1

print(alpha)
print(digit)
print(special_char)


