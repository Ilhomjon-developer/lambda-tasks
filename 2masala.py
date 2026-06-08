#masala - 3
C = input("C belgisini kiriting: ")
S = input("S satrini kiriting: ")

natija = ""

for harf in S:
    if harf == C:
        natija += harf * 2
    else:
        natija += harf

print("Natija:", natija)
#masala - 4
C = input("C belgisini kiriting: ")
S1 = input("S1 satrini kiriting: ")
S2 = input("S2 satrini kiriting: ")

natija = ""

for harf in S1:
    if harf == C:
        natija += S2 + harf
    else:
        natija += harf

print("Natijasi:", natija)