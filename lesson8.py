#masala - 1
def process_words(text: str):
    words = text.split(' ')
    result_words = []
    
    for word in words:
        if not word: 
            result_words.append(word)
            continue
            
        first_char = word[0] 
        new_word = first_char 
        
        for char in word[1:]:
            if char.lower() == first_char.lower():
                new_word += '.'
            else:
                new_word += char
                
        result_words.append(new_word)
        
    return ' '.join(result_words) 

print(process_words("minimum"))          
print(process_words("lola va boychechak")) 

#masala - 2
def process_last_char(text: str):
    words = text.split(' ')
    result_words = []
    
    for word in words:
        if not word: 
            result_words.append(word)
            continue
            
        last_char = word[-1]
        new_word = ""
        
        for char in word[:-1]:
            if char.lower() == last_char.lower():
                new_word += '.'
            else:
                new_word += char
          
        new_word += last_char
        result_words.append(new_word)
        
    return ' '.join(result_words)  

print(process_last_char("minimum"))         
print(process_last_char("toshkent va kuku"))

#masala - 3
def reverse_word_order(text: str) -> str:
    words = text.split(' ')
    actual_words = [w for w in words if w][::-1]
    
    result_words = []
    word_index = 0
    
    for w in words:
        if w == '':
            result_words.append('')
        else:
            result_words.append(actual_words[word_index])
            word_index += 1
            
    return ' '.join(result_words)

print(reverse_word_order("bugun havo ajoyib")) 
print(reverse_word_order("men   kod   yozdim")) 

#masala - 4
def sort_words_alphabetically(text: str):
    words = text.split()
    sorted_words = sorted(words)

    return " ".join(sorted_words)

test_text = "OLMA    ANOR   BEHI    ANJIR"
print("Asl holati:   ", test_text)
print("Saralangani:  ", sort_words_alphabetically(test_text))

#masala - 5
def capitalize_words(text: str):

    words = text.split(' ')
    result_words = []
    
    for word in words:
        if not word:
            result_words.append(word)
        else:
            new_word = word[0].upper() + word[1:]
            result_words.append(new_word)
            
    return ' '.join(result_words)

test_text = "bugun   codeTech loyihasi ustida ishlaymiz"
print("Asl matn: ", test_text)
print("Natija:   ", capitalize_words(test_text))

#masala - 6
def count_punctuations(text: str) -> int:
    punctuations = ".,!?;:-()\"'"
    count = 0
    
    for char in text:
        if char in punctuations:
            count += 1 
    return count

test_text = "Salom, Ilhomjon! Bugun havo ajoyib: quyoshli va issiq."
print("Matn:", test_text)
print("Tinish belgilari soni:", count_punctuations(test_text))

#masala - 7
def count_letters(text: str):
    count = 0

    for char in text:
        if char.isupper():
            count += 1 
    return count

test_text = "CodeTech Intelligence Global Holding"
print("Matn:", test_text)
print("Katta harflar soni:", count_letters(test_text))

#masala - 8
def find_longest_word(text: str):
    words = text.split()
    if not words:
        return ""
        

    longest = max(words, key=len)
    return longest

test_text = "Dasturlash markazida mukammal backend darslari bo'lmoqda"
print("Matn:", test_text)
print("Eng uzun so'z:", find_longest_word(test_text))

#masala - 9
def find_short_word(text: str):
    words = text.split()
    if not words:
        return ""
    shortest = min(words[::-1], key=len)
    return shortest


test_text = "Dasturlash va kodlash bu kelajak"
print("Matn:", test_text)
print("Eng qisqa so'z (oxirgisi):", find_short_word(test_text))

#masala - 10
def remove_extra_spaces(text: str):
    words = text.split()
    return " ".join(words)
test_text = "   Men   CodeTech   kompaniyasida   backend   dasturchiman.   "
print("Asl holati:   ", f"'{test_text}'")
print("Tozalangani:  ", f"'{remove_extra_spaces(test_text)}'")

#masala - 11
def get_file_name(file_path: str):

    full_file_name = file_path.split('\\')[-1]
    file_name = full_file_name.split('.')[0]
    return file_name

test_path = r"D:\Python_c++\books\My_book.exe"
print("Faylning to'liq yo'li:", test_path)
print("Fayl nomi:             ", get_file_name(test_path))