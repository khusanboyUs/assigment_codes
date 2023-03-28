#Find the anonymous function in the given array and use the function to process the rest members of array (like map does)
#So, as the short task summary:
#We have one list with some element being an function object.
#We don't know what is the index of that function object in the list.
#We need to locate that function and use it against all other list items.

def find_lambda(list_):
    return []

#print(find_lambda([lambda a: a+2,9,3,1,0])) # [11, 5, 3, 2]
#print(find_lambda([9,2,3,lambda a: a/2.0,1,0])) #[4.5, 1, 1.5, 0.5, 0.0]


def find_lambda(list_):
    for i, elem in enumerate(list_):
        if callable(elem):
            func=elem
            break
    if func is None:
        return list_
    result=[]
    for elem in list_[i+1:]:
        result.append(func(elem))    
    return result

print(find_lambda([lambda a: a+2,9,3,1,0])) # [11, 5, 3, 2]
print(find_lambda([9,2,3,lambda a: a/2.0,1,0])) #[4.5, 1, 1.5, 0.5, 0.0]
                                    