#masala - 5
def string_oson(C, S1, S2):
    return S1.replace(C, C + S2)

print(string_oson("a", "banana", "lar"))
#masala - 6
def string_m(s1, s2):
    if s2 in s1:
        return True
    else:
        return False
print(string_m("banana", "nan"))