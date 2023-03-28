def super_shortify(str_):
    my_list=list(str_)
    result=[]
    if len(my_list) == 0 or len(my_list) ==1:
        return ''
    
    else:
        result.append('{}{}'.format(my_list[1],my_list[-2]))
           
    print(result)
    return ''.join(result)        
    

#print(super_shortify("aBc"))
def de_caesar(text, shift=13):
    result=''
    for i in range(len(text)):
        char=text[i]
        if (char.isupper()):
            result+=chr((ord(char)+shift-65)%26+65)
        elif char == '!':
            result+=char 
        elif char.isspace():
            result+=char       
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97) 
    return result           
    
    
#print(de_caesar("Lbh tbg vg!", 13))  # You got it!
#
elevator_records = [
    {2: 3, 4: 5, 5: 2, 6: 5},
    {1: 5, 2: -1, 4: -2, 5: 1, 6: -3},
    {1: 1, 2: 3, 3: 1, 4: 1, 5: 1, 6: 2},
    {1: -1, 2: -1, 3: 1, 4: 1, 5: 1, 6: 3},
    {1: 1, 2: 3, 3: 1, 4: 1, 5: 1, 6: 1},
    {1: -2, 2: 3, 3: 1, 4: 1, 5: 1, 6: -1},
]

def elevator(elevator_records):
    # return MAX_ppl_floor, MAX_PPL, TotalPPL
    return 1, 1, 10
    
    
#print(elevator(elevator_records))
                                    
                                    
def find_lambda(list_):
    anonymous_func=list(filter(lambda x: callable(x),list_))[0]
    result=list(map(anonymous_func,filter(lambda x:x !=anonymous_func,list_ )))
    return result

#print(find_lambda([lambda a: a+2,9,3,1,0])) # [11, 5, 3, 2]
#print(find_lambda([9,2,3,lambda a: a/2.0,1,0])) #[4.5, 1, 1.5, 0.5, 0.0]
# 
test_data = ["az", "toto", "picaro", "zone", "kiwi"]

def partlist(list_):
    result=[]
    for words in test_data:
        print(words)
    return result    

#print(partlist(test_data))

list_ = [[[ [1, 4, 5], [[6, 9],[[[8, 1], 7], 3], 2], 7], 5, 2], 9, [1, 2]]

def rec_func(list_):
    total=0
    for item in list_:
        if type(item) == int:
            total+=item
        elif type(item) == list:
            total+=rec_func(item)
    return total                       

print (rec_func(list_))
                                    