#masala - 1
n = int(input(" sonini kiriting: "))
s = input("Satrni kiriting: ")

if len(s) > n:

    natija = s[-n:]
else:
    nuqta = '.'*(n - len(s))
    natija = nuqta + s 

print("Natija:", natija)
#masala - 2
n1 = int(input(" sonini kiriting: "))
n2 = int(input(" sonini kiriting: "))
s1 = input(" satrni kiriting: ")
s2 = input(" satrni kiriting: ")

qism1 = s1[:n1]
qism2 = s2[-n2:]
natija = qism1 + qism2

print("String Natijasi:", natija)




