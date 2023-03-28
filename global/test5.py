def fizzbuzz():
    result=[]
    for i in range(1,100):
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
# Test
def is_curzon(num):
    first_number=pow(2,num)+1
    second_number=2*num+1

    if (first_number % second_number)==0:
        return True
    else:
        return False
    
#print(is_curzon(5)) # True
#print(is_curzon(10)) # False



def check(target: str, list_):
    if len(list_) == 0:
        return False
    
    for words in list_:
        if words.lower() == target.lower():
            return True
        else:
            return False    
    
    
print(check("a", ["A", "b", "c"]))  # True
print(check("abc", ["AbC", "b", "c"]))  # True
print(check("aBc", ["AbC"]))  # True
print(check("abc", ["a", "b", "c"]))  # False
print(check("abc", []))  # False
                                                                        

                      