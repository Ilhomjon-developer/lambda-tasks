#masala - 1
def satrlar(fayl):
    with open(fayl, 'r',encoding='utf-8') as file:
        for i in file:
            yield i.strip()

generator = satrlar('vazifa.txt')
print(next(generator))

#masala - 2
def juftlar(fayl):
    with open(fayl, 'r') as file:
        for i in file:
            son = int(i.strip())
            if son % 2 == 0:
                yield son
gener = juftlar('numbers.txt')

print(next(gener))

#masala - 3
def uzun_generator(fayl_nomi):
    with open(fayl_nomi, 'r', encoding='utf-8') as file:
        for line in file:
            matn = line.strip()
            if len(matn) > 5:
                yield matn
genera = uzun_generator('text.txt')
print(next(genera))
print(next(genera))
            

#masala - 4
def kvadratlar(fayl_nomi):
    with open(fayl_nomi, 'r') as file:
        for line in file:
            son = int(line.strip())
            yield son ** 2
gen = kvadratlar('nums.txt')
print(next(gen))

#masala - 5
def sozlar(fayl_nomi):
    with open(fayl_nomi, 'r', encoding='utf-8') as file:
        for line in file:
            sozlar = line.strip().split() 
            for soz in sozlar:
                yield soz
soz = sozlar('words.txt')
print(next(soz))
#masala  - 6
import psycopg2

def players_generator():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="7879",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT id , full_name FROM players ")

    for row in cur:
        yield row

    conn.close()

for player in players_generator():
    print(player)

#masala - 7

def products_generator():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="7879",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM products WHERE price > 10000")

    for row in cur:
        yield row

    conn.close()
for i in products_generator():
    print(i)

#masala - 8

def users_generator():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="7879",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT email FROM users")

    for row in cur:
        yield row

    conn.close()

for i in users_generator():
    print(i)

#masala - 9

eng_uzun_ism = ""
def users_generators():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="7879",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT name FROM users")
   
    for row in cur:
        yield row[0]

    conn.close()
uzun_ism = ""   
for ism in users_generators():
    if len(ism) > len(uzun_ism):
        uzun_ism = ism
    print(uzun_ism)
    
#masala - 10

def players_generator(start, stop):
    conn = psycopg2.connect(
        dbname="n84_db",
        user="postgres",
        password="3698",
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM products OFFSET %s LIMIT %s",
        (start, stop)
    )

    result = cur.fetchall()

    cur.close()
    conn.close()

    yield result


start = 0
limit = 5

for i in range(20):
    test = players_generator(start, limit)

    print(next(test))

    start += 5
