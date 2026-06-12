
#masala - 1
s = lambda x,y: x + y
print(s(4,5))
#masala - 2
k = lambda x : x **2
print(k(5))
#masala - 3
a = lambda x : "juft" if x % 2 == 0 else "toq"
print(a(4))
#masala - 4
b = lambda matn: len(matn)
print(b("olma"))
#masala - 5
c = lambda ism: f" Salom {ism}"
print(c("Ilhomjon"))
#masala - 6
royxat = [5,2,9,1]
d = sorted(royxat, key=lambda x: x)
print(d)
#masala - 7
talabalar = [
    {"ism": "Ali", "ball": 85},
    {"ism": "Vali", "ball": 95},
    {"ism": "Hasan", "ball": 75}
]
e = sorted(talabalar, key=lambda x: x["ball"])
print(e)
#masala - 8
sozlar = ["olma", "anor", "shaftoli", "behi"]
f = sorted(sozlar,key=lambda x: len(x))
print(f)
#masala - 9
nuqtalar = [(1, 4), (3, 1), (5, 9)]
g = sorted(nuqtalar,key=lambda x: x[1])
print(g)
#masala - 10
mahsulotlar = [
    {"nomi": "Olma", "narxi": 15000},
    {"nomi": "Banan", "narxi": 22000},
    {"nomi": "Anor", "narxi": 18000}
]
h = sorted(mahsulotlar,key=lambda x: x["narxi"])
print(h)
#masala - 11
talabalar = [
    {"ism": "Ali", "ball": 85},
    {"ism": "Vali", "ball": 95},
    {"ism": "Hasan", "ball": 75}
]
j = sorted(talabalar, key=lambda x: x["ball"], reverse=True)
print(j)
#masala - 12
sonlar = [17, 42, 99, 20]
k = sorted(sonlar, key=lambda x: x % 10)
print(k)
#masala - 13
fayllar = [
    {"nomi": "rasm.png", "hajmi": 5},    # 5 MB
    {"nomi": "kino.mp4", "hajmi": 700},  # 700 MB
    {"nomi": "kod.py", "hajmi": 2}       # 2 MB
]
l = sorted(fayllar, key=lambda x: x["hajmi"], reverse=True)
print(l)
#masala - 14
guruh = [
    {"ism": "Ali", "yosh": 20, "ball": 85},
    {"ism": "Vali", "yosh": 19, "ball": 95},
    {"ism": "Hasan", "yosh": 20, "ball": 90}
]
m = sorted(guruh, key=lambda x: (x["yosh"],x["ball"]))
print(m)
#masala - 15
odamlar = ["Ilhom Ahmadjonov", "John Doe", "Ali Valiyev", "Hasan Toshmatov", "Asror Qodiriy"]
n = sorted(odamlar, key=lambda x: x.split()[-1][-1])
print(n)
#masala - 16
k = lambda x : x **3
print(k(5))
#masala - 17
ismlar = ["Ali", "Ilhomjon", "Zuhra", "Olim"]
l = sorted(ismlar,key=lambda x: len(x),reverse=True)
print(l)
#masala - 18
mahsulotlar = ["Banan", "Olma", "Anor", "Gilos"]
o = sorted(mahsulotlar,key=lambda x:x[0])
print(o)
#masala - 19
gap = "Python dasturlash tili juda ajoyib"
p = sorted(gap.split(),key=lambda x:len(x))
print(p)
#masala - 20
sonlar = [45, 12, 89, 3, 67, 21]
q = lambda sonlar: [(max(sonlar),min(sonlar))]
print(q(sonlar))
