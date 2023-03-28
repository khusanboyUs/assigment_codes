#create function to reverse the string
#create function to extract int from str
#create fnction to detect if first letter is title

#create testcases to test if they are working as intended
#conclusion

def string_reverser(my_word:str)->str:
    return my_word[::-1]

def my_string_int(my_word):
    result=[]
    for words in my_word:
        if words.isdigit():
            result.append(words)

    return "".join(result)

def check_upper(my_word):
    return my_word.istitle() 

class TestMethod:
    def test_case1(self):
        assert string_reverser('krakow') == 'wokark'

    def test_case2(self):
        assert my_string_int('gl34obal') == '34'

    def test_case3(self):
        assert check_upper('Globallogic') == True        
