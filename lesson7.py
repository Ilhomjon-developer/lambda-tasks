#masala - 1

from datetime import datetime
import time

s1 = 'maxanizatsiyalashmagan'
s2 = 'a'
s3 = 'x'

def s2_index(s1):
    for index, harf in enumerate(s1):   
        if harf == s2:
            yield index

gen = s2_index(s1)


for i in gen:
    print(i)
    
  

def deco(func):
    def wrapper(s1, s2, s3):
        print(f'Func start: {datetime.now()}')
        print(f"Funksiya almashtisihlar soni 1")
        s1 = s1[::-1]
        s1 = s1.replace(s2, s3, 1)
        s1 = s1[::-1]

        return func(s1, s2, s3)
        
    return wrapper


@deco
def replace_s2_s3(s1, s2, s3):
    return s1

print(replace_s2_s3(s1, s2, s3))


#masala - 2

s1 = 'backend chiroyli, backend premium'
s2 = 'backend'
s3 = 'CodeTech'

def s2_index_generator(s1, s2):
    start = 0
    while True:
        pos = s1.find(s2, start)
        if pos == -1: 
            break
        yield pos
        start = pos + len(s2) 

def deco(func):
    def wrapper(s1, s2, s3):
        start_time = time.time() 
       
        jami_topildi = len(list(s2_index_generator(s1, s2))) 
        
        yangi_s1 = s1.replace(s2, s3)
        
        end_time = time.time() 
        
        print(f"Bajarilish vaqti: {end_time - start_time} soniya")
        print(f"Almashtirilgan elementlar soni: {jami_topildi}")
        print(f"Natijaviy satr uzunligi: {len(yangi_s1)}")
        
        return yangi_s1
    return wrapper

@deco
def replace_all(s1, s2, s3):
    return s1

print("Natija:", replace_all(s1, s2, s3))       

#masala - 3

def space_index_generator(s1):
    start = 0
    while True:
        pos = s1.find(" ", start)
        if pos == -1:
            break
        yield pos
        start = pos + 1

def deco_space(func):
    def wrapper(s1):
        start_time = time.time()
 
        indekslar = list(space_index_generator(s1))
        if len(indekslar) >= 2:
            natija_matn = s1[indekslar[0] + 1 : indekslar[1]]
        else:
            natija_matn = ""
            
        end_time = time.time()
        
        print(f"Bajarilish vaqti: {end_time - start_time:.6f} soniya")
        print(f"Ajratib olingan belgilar soni: {len(natija_matn)}")
        
        return natija_matn
    return wrapper

@deco_space
def get_between_spaces(s1):
    return s1

matn = "CodeTech Intelligence Global Holding"
print("Natija:", get_between_spaces(matn))

#masala - 4

def space_index_generator_v2(s1):
    start = 0
    while True:
        pos = s1.find(" ", start)
        if pos == -1:
            break
        yield pos
        start = pos + 1

def deco_last_space(func):
    def wrapper(s1):
        indekslar = list(space_index_generator_v2(s1))
        if len(indekslar) >= 2:
            yangi_matn = s1[indekslar[0] + 1 : indekslar[-1]]
        else:
            yangi_matn = ""
      
        print(f"Natijaviy qism uzunligi: {len(yangi_matn)} ta belgi")
        
        return yangi_matn
    return wrapper

@deco_last_space
def get_between_first_and_last(s1):
    return s1

matn_test = "CodeTech Intelligence Global Holding" 
print("Natija:", get_between_first_and_last(matn_test))

#masala - 5
def word_generator(s1):
    sozlar_royxati = s1.split()
    for soz in sozlar_royxati:
        yield soz

def deco_word_count(func):
    def wrapper(s1):
        start_time = time.time()
        jami_sozlar = list(word_generator(s1))
        sozlar_soni = len(jami_sozlar)
        end_time = time.time()

        print(f"Bajarilish vaqti: {end_time - start_time:.6f} soniya")
        print(f"Topilgan so'zlar soni: {sozlar_soni} ta")
        
        return sozlar_soni
    return wrapper

@deco_word_count
def count_words(s1):
    return s1

matn_test = "CodeTech Intelligence Global Holding backend tizimlari"
print("Natija (So'zlar soni):", count_words(matn_test))

#masala - 6

def word_generator_v2(s1):
    sozlar = s1.split()
    for soz in sozlar:
        yield soz

def deco_same_letter(func):
    def wrapper(s1):
        jami_sozlar = list(word_generator_v2(s1))
        mos_sozlar_soni = 0
        for soz in jami_sozlar:
            if len(soz) > 0 and soz[0] == soz[-1]:
                mos_sozlar_soni += 1

        print(f"Shartga mos kelgan so'zlar soni: {mos_sozlar_soni} ta")
        
        return mos_sozlar_soni
    return wrapper

@deco_same_letter
def check_letters(s1):
    return s1

matn_test = "ODAM CODETECH IKKI NON" 
print("Natija:", check_letters(matn_test))

#masala - 7

def word_generator_v3(s1):
    for soz in s1.split():
        yield soz

def deco_find_a(func):
    def wrapper(s1):
        jami_sozlar = list(word_generator_v3(s1))
        
        tekshirilgan_jami = len(jami_sozlar)
        mos_sozlar_soni = 0
        
        for soz in jami_sozlar:
            if "A" in soz:
                mos_sozlar_soni += 1

        print(f"Tekshirilgan jami so'zlar soni: {tekshirilgan_jami} ta")
        print(f"Kamida bitta 'A' harfi bor so'zlar soni: {mos_sozlar_soni} ta")
        
        return mos_sozlar_soni
    return wrapper

@deco_find_a
def count_words_with_a(s1):
    return s1

matn_test = "CODETECH INTELLECTUAL GLOBAL HOLDING BACKEND DEVELOPMENT"
print("Natija:", count_words_with_a(matn_test))

#masala - 8

def word_generator_v4(s1):
    for soz in s1.split():
        yield soz

def deco_exactly_three_a(func):
    def wrapper(s1):
        jami_sozlar = list(word_generator_v4(s1))
        mos_sozlar_soni = 0
        
        for soz in jami_sozlar:
            if soz.count("A") == 3:
                mos_sozlar_soni += 1
        print(f"Aniq 3 ta 'A' harfi mavjud bo'lgan so'zlar soni: {mos_sozlar_soni} ta")
        
        return mos_sozlar_soni
    return wrapper

@deco_exactly_three_a
def count_exact_three_a(s1):
    return s1

matn_test = "AVTAMAT  BANANA APP CODETECH ARABISTON"
print("Natija:", count_exact_three_a(matn_test))

#masala - 9

def word_generator_v5(s1):
    for soz in s1.split():
        yield soz

def deco_shortest_word(func):
    def wrapper(s1):
        jami_sozlar = list(word_generator_v5(s1))
        
        if not jami_sozlar:
            return ""
        eng_qisqa = min(jami_sozlar, key=len)

        print(f"Eng qisqa so'zning uzunligi: {len(eng_qisqa)} ta belgi")
        
        return eng_qisqa
    return wrapper

@deco_shortest_word
def find_shortest(s1):
    return s1

matn_test = "CodeTech premium backend tizimi eng kuchli platformadir"
print("Natija (Eng qisqa so'z):", find_shortest(matn_test))

#masala - 10

def word_generator_v6(s1):
    for soz in s1.split():
        yield soz

def deco_longest_word(func):
    def wrapper(s1):
        jami_sozlar = list(word_generator_v6(s1))
        
        if not jami_sozlar:
            return ""

        teskari_sozlar = jami_sozlar[::-1]
        eng_uzun = max(teskari_sozlar, key=len)

        print(f"Eng uzun so'zning uzunligi: {len(eng_uzun)} ta belgi")
        
        return eng_uzun
    return wrapper

@deco_longest_word
def find_longest(s1):
    return s1

matn_test = "CodeTech Intelligence Global Holding premium backend Platformadir"
print("Natija (Oxirgi eng uzun so'z):", find_longest(matn_test))

#masala - 11

def word_generator_v7(s1):
    for soz in s1.split():
        yield soz

def deco_dot_join(func):
    def wrapper(s1):

        jami_sozlar = list(word_generator_v7(s1))
        sozlar_soni = len(jami_sozlar)
        natija_satr = ".".join(jami_sozlar)

        print(f"Topilgan so'zlar soni: {sozlar_soni} ta")
        print(f"Natijaviy satr uzunligi: {len(natija_satr)} ta belgi")
        
        return natija_satr
    return wrapper

@deco_dot_join
def format_with_dots(s1):
    return s1

matn_test = "CodeTech Intelligence Global Holding backend tizimlari"
print("Natija:", format_with_dots(matn_test))