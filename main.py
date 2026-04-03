#1
katta = lambda a, b: a if a > b else b

res = katta(2, 7)
print(res)


#2
modul = lambda x: x if x >= 0 else -x

res = modul(-10)
print(res)


#3
perimetr = lambda a, b, c: a + b + c

res = perimetr(3, 7, 2)
print(res)


#4
qoldiq = lambda a, b: a % b

res = qoldiq(15, 2)
print(res)


#5
faran = lambda c: c * 9/5 + 32

res = faran(100)
print(res)
