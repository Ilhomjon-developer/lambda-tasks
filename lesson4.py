# Masala - 1

from collections import namedtuple

Student = namedtuple('Student',('name', 'age', 'group'))
name = input("Ismingizni kiriting: ")
age = int(input("Yoshingizni kiriting: "))
group = input("Guruhingizni kiriting: ")
talaba = Student(name=name, age=age,group=group)

print(f"Talaba ismi {talaba.name} Talaba yoshi {talaba.age} Talabaning guruhi {talaba.group}")


# Masala - 2

Book = namedtuple('Book',('title', 'author', 'year'))
book = Book('0 dan 1 ga','Piter Theil','2014')

print(book.author)


# Masala - 3

Point = namedtuple('Point',('x', 'y'))
nuqta = Point(10, 20)

print(nuqta.x)
print(nuqta.y)


# Masala - 4

Car = namedtuple('Car', ('brand', 'model', 'year'))
car = Car('Chevrolet', 'Cobalt', '2024')

print(f"Mashina brandi: {car.brand}, Mashina modeli: {car.model}, Mashina yili: {car.year}")


# Masala - 5

Student = namedtuple('Student',('name', 'age', 'score'))

talabalar = [
    Student('Ali', 20, 85),
    Student('Vali', 21, 92),
    Student('Sardor', 19, 78),
    Student('Madina', 22, 95),
    Student('Diyor', 20, 88)
]
ball = max(talabalar,key=lambda x: x.score)
print(ball)


# Masala - 6

Product = namedtuple('Product', ('name', 'price', 'quantity'))
mahsulotlar = [
    Product('Osh', 45000, 3),    
    Product('Choy', 5000, 5),     
    Product('Manti', 8000, 10)    
]
result = sum([ m.price * m.quantity for m in mahsulotlar])
print(result)


# Masala - 7

Employee =namedtuple('Employee', ('name', 'salary'))

xodim1 = Employee("Eshmat", 1000000)

xodim2 = xodim1._replace(salary = xodim1.salary * 1.2)
print(xodim1,xodim2)


# Masala - 8

City = namedtuple('City', ('name', 'population'))

shaharlar = [
    City('Tashkent', 3000000),
    City('New York', 8500000),
    City('Moscow', 13000000),
    City('Samarkand', 550000),
    City('Bukhara', 280000),
    City('Andijan', 450000),
    City('Tokyo', 14000000),
    City('Khiva', 95000),
    City('Navoiy', 160000),
    City('London', 9000000)
]
print([i for i in shaharlar if i.population > 1000000])


# Masala - 9

Student = namedtuple('Student', ('name', 'faculty', 'gpa'))

talabalar = [
    Student('Ali', 'IT', 3.8),
    Student('Vali', 'IT', 3.5),
    Student('Sardor', 'Economics', 3.2),
    Student('Madina', 'Medicine', 3.9),
    Student('Diyor', 'IT', 3.6),
    Student('Zuhra', 'Medicine', 3.7),
    Student('Nodir', 'Economics', 2.9),
    Student('Shaxzod', 'IT', 3.4),
    Student('Malika', 'Medicine', 4.0),
    Student('Jasur', 'Economics', 3.1),
    Student('Kamola', 'IT', 3.9),
    Student('Farrux', 'Economics', 3.5),
    Student('Go`zal', 'Medicine', 3.6),
    Student('Olim', 'IT', 3.2),
    Student('Aziza', 'Economics', 3.8),
    Student('Bekzod', 'Medicine', 3.3),
    Student('Laylo', 'IT', 3.7),
    Student('Rustam', 'Economics', 3.0),
    Student('Dilshod', 'Medicine', 3.5),
    Student('Zarina', 'Economics', 3.6)
]

groups = {}

for s in talabalar:

    if s.faculty not in groups:
        groups[s.faculty] = []

    groups[s.faculty].append(s.gpa)

for f, gpas in groups.items():
    print(f, f"{sum(gpas) / len(gpas)}")


# Masala - 10

Order = namedtuple('Order', ('order_id', 'customer', 'amount'))

buyurtmalar = [
    Order(1, 'Ali', 450000),
    Order(2, 'Vali', 1200000),      
    Order(3, 'Ali', 300000),        
    Order(4, 'Olim', 1500000),     
    Order(5, 'Vali', 200000),       
    Order(6, 'Madina', 80000),
    Order(7, 'Olim', 250000)        
]

summa = [o.amount for o in buyurtmalar]
katta = max(summa)
kichik = min(summa)
ortacha = sum(summa) / len(summa)
soni = len([o for o in buyurtmalar if o.amount > 1000000])
mijoz_pullari = {}
for o in buyurtmalar:
    if o.customer not in mijoz_pullari:
        mijoz_pullari[o.customer] = 0
    mijoz_pullari[o.customer] += o.amount
vip_mijoz = max(mijoz_pullari, key=lambda k: mijoz_pullari[k])

print(f"Eng kattasi {katta}")
print(f"Eng kichigi {kichik}")
print(f"Ortachasi {ortacha}")
print(f"Buyurtma soni {soni}")
print(f"Kop pul sariflagan mijoz {vip_mijoz}") 
