

def method_one(string):
    return string[::-1]


def method_two(string):
    my_list=list(string)
    words=my_list.reverse()
    result="".join(my_list)
    return result


def method_three(string):
    string2=''.join(reversed(string))
    return string2

#testing

class TestClass:
    def test_one_1(self):
        assert method_one('warsaw') == 'wasraw'

    def test_one_2(self):
        assert method_two('krakow') == 'wokark'

    def test_one_3(self):
        assert method_three('gdansk') == 'ksnadg'

    def test_one_4(self):
        assert method_three('warsaw') == method_one('warsaw')

    def test_one_5(self):
        assert method_two('super') == method_one('super')    

#second solution


test_strings = ["kawabunga", "metro2013", "moon", "orange"]

def shwalengthimeter2(test_strings):
    my_result=[]
    vowels=["a", "e", "o", "i", "u", "y","r"]
    for words in test_strings:
       my_word=list(words)
       length=len(my_word)
       my_word.pop(0) 
       if my_word[0] in vowels:
           my_word.pop(0)
       my_word.insert(0,'shwa')
       to_string="".join(my_word)
       pre_words=f'{to_string} {length}'
       my_result.append(pre_words)
         
    return my_result      

           


def shwalengthimter(test_strings):
    new_list = []

    for i in test_strings:
        length = len(i)
        i = i[1:]
        if i[0] in ["a", "e", "o", "i", "u", "y"]:
            i = i[1:]
        new_list.append('shwa' + i + " " + str(length))

    return new_list




# Narcissistic Numbe test
def narcissistic(test_number):
    nums=[int(x) for x in str(test_number)]
    l=len(nums)
    counter=0
    lis=[]
    while counter <=0:
        for i in nums:
            lis.append(i**int(l))
        counter+=1
    sums=sum(list(lis))
    total=[int(x) for x in str(sums)]
    if nums == total:
        return True
    else:
        return False
    
#print(narcissistic(371))  # True
#print(narcissistic(371)) # True
#print(narcissistic(122)) # False
#print(narcissistic(4887)) # False


data = '''
        "SuperMaxCapacity" =0
        "MaxCapacity": 4540
        'CurrentCapacity'=   2897
        "LegacyBatteryInfo" = {"Amperage"=18446744073709550521,"Flags"=4,"Capacity"=4540,"Current"=2897,"Voltage"=7283,"Cycle Count"=406}
        "MegaMaxCapacity" = 6700
'''

def get_battery_level(data):
    data=data.split()
    max=data[3]
    current=data[5]
    if '+' and ';' in data[3]:
        print('yes')
    result=int(current) / int(max)
    print("{:.2%}".format(result))
    

p=get_battery_level(data)
