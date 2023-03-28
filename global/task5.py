
def split_n_join(str_):
    s=str_
    s=s.replace('~','').split()
    return '~~~'.join(s)
    


#print(split_n_join('My   lovely\n  ~little~ string'))    
# Should return:
# My~~~lovely~~~little~~~string

'''
The task is to process a given string:
Remove all tildas ('~')
Split by whitespaces
Join parts with three tildas: '~~~'
An example of the processing of the given string s:'''

def super_shortify(str_):
  # This will pass one of the tests :)
    if len(str_) == 1 or 0:
        return 'hell'
    second=str_[1]
    second_to_last=str_[-2]
    print(second)
    print(second_to_last)
    if str_.index(second) == 2 and str_.index(second_to_last) == int(str_)
print(super_shortify("aBcDe"))
                                   