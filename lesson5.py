#masala - 1

def my_func(func):
    def wrapper(*args, **kwargs):
        print("=== Start ===")
        result = func(*args, **kwargs)
        print("=== End ===")
        return result
    return wrapper

@my_func
def salom():
    print("Salom")

salom()

#masala - 2

def  show(func):
    def wrapper(*args, **kwargs):
        print(f"{args}")
        return func(*args)
    return wrapper

@show
def add(a,b):
    return a + b

print(add(30, 70))

#masala - 3

def get_func(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2
    return wrapper

@get_func
def son():
    return 15

print(son())

#masala - 4
def filter(func):
    def wrapper(lst):
        lsti = [x for x in lst if x > 0]
        return func(lsti)
    return wrapper

@filter
def show_list(lst):
    print(lst)
show_list([-5, 3, -2, 10, 7])

#masala - 5

def count_calls(func):
    count = 0  

    def wrapper(*args, **kwargs): 
        nonlocal count  
        count += 1

        print(f"Funksiya {count} marta chaqirildi")

        return func(*args, **kwargs)

    return wrapper

@count_calls
def salom():
    print("Salom dunyo")

salom()
salom()
salom()

#masala - 6

def juft(func):
    def wrapper(lst):
        juftlar = [x for x in lst if x % 2 == 0]
        return func(juftlar)
    return wrapper
@juft
def show(lst):
    return lst
print(show([2, 3, 4, 6, 7, 8]))

#masala - 7

import time
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{end_time - start_time} sekund")
        return result
    return wrapper
@timer
def task():
    time.sleep(0.5)
task()

#asala - 8

def sort(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if isinstance(res, list):
            return sorted(res)
        return res
    return wrapper
@sort
def data():
    return[5, 2, 8, 1]
print(data())
    
#masala - 9

def double(func):
    def wrapper(lst):
        return func([x for x in lst if x > 0])
    return wrapper
def double2(func):
    def wrapper(lst):
        return func([x for x in lst if x > 10])
    return wrapper
@double
@double2
def nums(lst):
    return lst
print(nums([-5, 3, 11, 15, -20, 7]))

#masala - 10

def multi_filter(func):
    def wrapper(lst):
        filtered = [x for x in lst if x > 0 and x % 2 == 0 and x > 10]
        return func(filtered)
    return wrapper

@multi_filter
def display(lst):
    return lst

print(display([-4, 12, 7, 20, -30, 11]))  

# #masala - 11

import time

def timer(func):
    def wrapper(*args, **kwargs):

        start = time.time() 
        result = func(*args, **kwargs)
        end = time.time()  
        x = end - start
        
        resp = f"Bajarilish vaqti: {x} sekund"
        print(f'Sekin ishlayapti: {resp}' if 1 < x else resp)

        return result
    return wrapper

@timer
def example():
    time.sleep(2)
    print("Funksiya tugadi")

example()

#masala - 12

def upper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result,str):
            return result.upper()
        return result
    return wrapper
@upper
def get():
    return "salom dunyo"
print(get())

#masala - 13

def pos_filter(func):
    def wrapper(lst):
        return func([x for x in lst if x > 0])
    return wrapper

def even_filter(func):
    def wrapper(lst):
        return func([x for x in lst if x % 2 == 0])
    return wrapper

def square_elements(func):
    def wrapper(lst):
        return func([x**2 for x in lst])
    return wrapper

@square_elements
@even_filter
@pos_filter
def final_process(lst):
    return lst

print(final_process([-2, 3, 4, 6, -8]))  

#masala - 14

import time
def logger(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        ras = func(*args, **kwargs)
        end = time.time()

        print(f"Funksiya: {func.__name__}")
        print(f"Args: {args}")
        print(f"Natija: {ras}")
        print(f"Vaqt: {end - start} sekund")
        return ras
    return wrapper
@logger
def add(a,b):
    return a + b
add(5, 7)

#masaala - 15

def decorator(func):
    def wrapper(x):
        return func(x) if isinstance(x, int) else "Funksiya integer qabul qiladi"
    
    return wrapper

@decorator
def test(x):
    return x

print(test('qwv'))

#masala - 16

def no_negative_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result < 0:
            raise ValueError("Xatolik: Funksiya natijasi manfiy bo'lishi mumkin emas!")
        return result
    return wrapper

@no_negative_result
def calc_balance(x,y):
    return x - y


print(calc_balance(200, 50)) 

#masala - 17

def decorator(func):
    def wrapper(x, y):
        result = func(x, y)
        with open('result.txt', 'a') as file:
            file.write(str(result)+'\n')
        
        return result 
    
    return wrapper


@decorator
def test(x, y):
    return x - y

print(test(202, 15))