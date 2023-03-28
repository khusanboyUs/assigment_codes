#dictionaries in python

my_vocab={
    'name':'Husanboy',
    'city':'Krakow',
    'year': 2002
    
}
my_vocab.update({'city':'Warsaw'})
print(my_vocab)
#my_vocab.pop('city') #popes with arguments
#print(my_vocab)
#my_vocab.popitem() # popes the last adedd iteams
#print(my_vocab)
#del my_vocab['name'] # deletes with arguments
#print(my_vocab)
#del my_vocab #deletes the whole dictionary


myFamily={
    'wife':{
        'name':'Anna',
        'year': 2003
    },
    'husband':{
        'name':'John',
        'year':2002
    },
    'son':{
        'name':'Mateusz',
        'year':2023
    }
}

#seperate it to modules   
'''
status=False

while status is False:
    search_name=str(input('Enter required username: '))
    for firstnames in myFamily.values():
        for names in firstnames.values():
            if search_name in firstnames.values():
                print('Available in {}'.format(firstnames.keys()))
                print('Completed')
            else:
                print('False')
status=True    

'''





namers={
    'Husan':20,
    'Adam':330
}
print(namers[0])