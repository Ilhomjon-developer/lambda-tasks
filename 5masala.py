#masala - 9
def string_funksiya(s1, s2):
    indeks = s1.find(s2)
    if indeks != -1: 
        return s1[:indeks]
    return s1 


print("Natijasi:", string_funksiya("CodeTech-Holding", "Tech"))
#masala - 10
def string_funksiya(s1, s2):
    indeks = s1.rfind(s2)
    if indeks != -1:
        return s1[:indeks]
    return s1


print("Natijasi:", string_funksiya("olma-anor-olma-uzum", "olma"))
