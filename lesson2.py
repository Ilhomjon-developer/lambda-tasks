#masala - 1
sonlar = [2, 5, 10, 15]
a = list(map(lambda x:x * 2, sonlar))
print(a)

#masala - 2
sonlar = [2, 5, 10, 15]
b = list(map(lambda x:x ** 2, sonlar))
print(b)

#masala - 3
sonlar = [2, 5, 10, 15]
c = list(map(lambda x:x + 10, sonlar))
print(c)

#masala - 4
sonlar = [2, 5, 10, 15]
d = list(map(lambda x: str(x),sonlar))
print(d)

#masala - 5
ismlar = ["ali", "vali", "ilhom"]
i = list(map(lambda x: x.upper(),ismlar))
print(i)

#masala - 6 
sonlar = [1, 2, 3, 4, 5, 6]
e = list(filter(lambda x: x % 2 == 0, sonlar))
print(e)

#masala - 7
sonlar = [1, -2, 3, 4, -5, 6]
f = list(filter(lambda x: x > 0, sonlar))
print(f)

#masala - 8
sonlar = [100, 120, 30, 4, -5, 60]
g = list(filter(lambda x: x > 50, sonlar))
print(g)

#masala - 9
sozlar = ["olma", "dasturlash", "python", "kitob"]
h = list(filter(lambda x: len(x) > 5, sozlar))
print(h)

#masala - 10
sonlar = [3, 5, 9, 12, 14, 15, 18, 20, 21]
m = list((filter(lambda x: x % 3 == 0, sonlar)))
print(m)

#masala - 11
sonlar = [1, 2, 3, 4]
n = list(map(lambda x: x ** 3, sonlar))
print(n)

#masala - 12
sonlar = [25, 38, 102, 44, 90]
o = list(map(lambda x: x % 10, sonlar))
print(o)

#masala - 13
ismlar = ["Ali", "Vali", "Ilhomjon"]
p = list(map(lambda x: len(x),ismlar))
print(p)

#masala - 14
sonlar = [1, 2, 6, 3, 4, 7, 5]
q = list(map(lambda x: "juft" if x % 2 == 0 else "toq",sonlar))
print(q)

#masala - 15
gap = "python va postgresql o'rganyapman"
r = list(map(lambda x: x.capitalize(),gap.split()))
print(r)

#masaala - 16
a = [13, 21, 67, 9, 11]
result = list(filter(lambda x: 2 == len([j for j in range(1, x+1) if x % j == 0]), a))
print(result)

#masala - 17
sonlar = [15, 48, 23, 95, 38]
s = list(filter(lambda x: (x // 10) + (x % 10) > 10,sonlar))
print(s)

#masala - 18
sozlar = ["non", "apple", "kiyik", "dasturchi", "radar"]
t = list(filter(lambda x: x==x[::-1],sozlar))
print(t)

#masala - 19
sonlar = [121, 45, 88, 345, 909, 7]
u = list(filter(lambda x: str(x)==str(x)[::-1],sonlar))
print(u)

#masala - 20
ismlar = ["Anvar", "Bobur", "Umid", "Ziyoda", "Eshmat", "Olim"]
y = list(filter(lambda x: x[0].lower() in "aeiou",ismlar))
print(y)

#masala - 21
from functools import reduce  

sonlar = [1, 2, 3, 4, 5]
v = reduce(lambda x, y: x + y, sonlar)
print(v)

#masala - 22
from functools import reduce  

sonlar = [1, 2, 3, 4, 5]
a = reduce(lambda x, y: x * y, sonlar)
print(a)

#masala - 23
from functools import reduce 

sozlar = ["CodeTech", "AI", "Holding"]
b = reduce(lambda x, y: x + " " + y, sozlar)
print(b)

#masala - 24
from functools import reduce 

sonlar = [14, 45, 8, 29]
c = reduce(lambda x, y: x if x > y else y,sonlar)
print(c)

# #masala - 25
ismlar = ["Anvar", "Umid", "Ziyoda"]
ballar = [85, 92, 78]
d = list(zip(ismlar, ballar))
print(d)

#masala - 26
oylar = ["Yanvar", "Fevral", "Mart"]
raqamlar = [1, 2, 3]
e = list(zip(oylar,raqamlar))
print(e)

#masala - 27
ismlar = ["Ali", "Vali"]
yoshlar = [20, 22]
guruhlar = ["Python-01", "Python-02"]
f = list(zip(ismlar,yoshlar,guruhlar))
print(f)

#masala - 28
mahsulotlar = ["Pizza", "Burger", "Cola"]
narxlar = [80000, 35000, 15000]
h = list(zip(mahsulotlar,narxlar))
print(h)

















