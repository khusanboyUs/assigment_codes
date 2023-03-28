#get the only evens
'''
for i, x in enumerate([5, 4, 7, 7, 2]):
    print(f"index: {i:2}{'(even)' if i%2==0 else '(odd)':7} --> {x}{'(even)' if x%2==0 else '(odd)':7}")
'''
def get_only_evens(list_: list) -> list:
    result=[]
    for i,nums in enumerate(list_):
        if i%2==0 and nums%2==0:
            result.append(nums)      
    return result
    
#assert get_only_evens([1, 3, 2, 6, 4, 8]) == [2, 4], "Wrong, #1"
#assert get_only_evens([0, 1, 2, 3, 4]) == [0, 2, 4], "Wrong, #2"
#assert get_only_evens([1, 2, 3, 4, 5]) == [], "Wrong, #3"
#assert get_only_evens([]) == [], "Wrong, #4"

#The task is to write a function which should generate a list with integers that in sum will give zero. For example, num is 3 and 5:
def gen_list(num):
    my_list=[]
    for i in range(1,num):
        my_list.append(i)

    sum_of_num=-abs(sum(my_list))
    my_list.append(sum_of_num)
    return my_list   

#print(gen_list(7))

#Important -- Don't modify original list and preserve original order. 
#If the smallest item is repeated only the first it's appearance should be removed
#remove_smallest([1,2,3,1,2])   # [2, 3, 1, 2]
#remove_smallest([5, 10, 3, 5, 3])   # [5, 10, 3, 5]

tests = [([1,2,3,4,5], [2,3,4,5]), ([5,4,1,3], [5,4,3]), ([1,2,1], [2,1])]

def remove_smallest(list_):
    my_list=list(list_)
    smallest=my_list[0]
    for x in list_:
        if x < smallest:
            smallest=x
    
    my_list.remove(smallest)
    return my_list        
    

#for test in tests:
    result = remove_smallest(test[0])
    assert result == test[1], "Wrong :("
    assert result is not test[0], "You can't change original list"


#Given few numbers, you need to return the digits that are not being used.
def unused_digits(*args):

    my_list=[]
    
    
#print(unused_digits(12, 34, 56, 78)) # "09"
#print(unused_digits(2015, 8, 26)) # "3479"
def sum_digits(input_str: str) -> int:
    my_list=list(input_str)
    #print(my_list)
    sum_list=[]
    numbers=[ num for num in range(0,10)]
    for char in my_list:
        if char in str(numbers):
            sum_list.append(int(char))       
    return sum(sum_list) 
   

    
    
# Small tests
#print(sum_digits("abc123___##05__5")) # 16
#print(sum_digits("00000000000")) # 0
#print(sum_digits("@@@@@@-1.0####")) # 1
#print(sum_digits("100____½")) # 1


def unused_digits(*args):
   unused="123456789"
   for i in args:
       for j in str(i):
           if j in unused:
               unused=unused.replace(str(j), '')
   return unused
        
    
print(unused_digits(12, 34, 56, 78)) # "09"
print(unused_digits(2015, 8, 26)) # "3479"

                                  
