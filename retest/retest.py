test_strings = ["kawabunga", "metro2013", "moon", "orange"]

def shwalengthimeter(test_strings):
    result=[]
    vowels=["a", "e", "o", "i", "u", "y"]
    for words in test_strings:
        my_string=words[1:]
        if my_string[0] in vowels:
            my_string=my_string[1:]
        result.append('shwa'+my_string+' '+str(len(words)))
    return result
            
    

#print(shwalengthimeter(test_strings))

def is_anagram(str1: str, str2: str) -> bool:
    str1=str1.lower()
    str2=str2.lower()
    if len(str1)==len(str2):
        str1_l=sorted(list(str1))
        str2_l=sorted(list(str2))
        return str1_l == str2_l
    else:
        return False
        
        
    
#print(is_anagram("AbbA", "BBaA")) # True

songs_db = [ {
 'artist': 'Led Zeppelin', 
 'title': 'Stairways to heaven', 
 'playback': '09:00' 
}, {
 'artist': 'Metallica', 
 'title': 'Master of puppets', 
 'playback': '04:30' 
}, {
 'artist': 'Nirvana', 
 'title': 'The Man who sold the world', 
 'playback': '03:10' 
}, {
 'artist': 'Stepan Galyabarda', 
 'title': 'Lyst do mamy', 
 'playback': '09:20' 
}]

def get_song(db, len_seconds):

   data=sorted(
       db,
       reverse=True,
       key=lambda a: dj_helper(a['playback']) 
   )
   print(data)
   for music in data:
       if dj_helper(music['playback']) <= len_seconds:
           return 'Best possible song: {}/{}'.format(music['artist'],music['title'])
   else:
        return False
       
def dj_helper(playback):
   m,s=playback.split(':')
   return int(m)*60+int(s)  

#print(get_song(songs_db, 145))
def check(target: str, list_):
    if len(list_) == 0:
        return False
    
    
    for words in list_:
        if words.lower() == target.lower():
            return True
    else:
        return False  
    
''' 
print(check("a", ["A", "b", "c"]))  # True
print(check("abc", ["AbC", "b", "c"]))  # True
print(check("aBc", ["AbC"]))  # True
print(check("abc", ["a", "b", "c"]))  # False
print(check("abc", []))  # False
'''
def unused_digits(*args):
    used=[]
    for arg in args:
        used.extend([int(digit) for digit in str(arg)])
    all_digits=[x for x in range(0,10)]
    unused=[digit for digit in all_digits if digit not in used]
    return "".join([str(digit) for digit in unused])    
        
    
#print(unused_digits(12, 34, 56, 78)) # "09"
#print(unused_digits(2015, 8, 26)) # "3479"

def fizzbuzz():
    result=[]
    for i in range(1,101):
        if i%3==0 and i%5==0:
            result.append('FizzBuzz')
        elif i%3==0:
            result.append('Fizz')
        elif i%5==0:
            result.append('Buzz')
        else:
            result.append(i)
    return result

#print(fizzbuzz()[:20])

def draw_table():
    x=1
    while x<10:
        y=1
        while y<10:
            print("%4d" % (x*y), end='')
            y+=1
        print() 
        x+=1
         


    
draw_table()