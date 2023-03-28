#Remove several (given number) - smallest - items from given list.
#Don't modify original list and preserve original order.
#First parameter is number of items to remove, second one - original list.

'''
tests = [
    (3, [1,2,3,1,2,4], [3,2,4]), 
    (2, [5,4,1,3], [5,4]), 
    (4, [1,2,1], [])
]

def remove_smallest(num, list_):
    for numbers in list_[:len(list_)]:
        if (numbers == min(list_)):
            list_.remove(numbers)
    for numbers in list_:
        if len(list_) ==1:
            list_.remove(numbers)            
            
                
    return list_[:num]       

for test in tests:
    number, original, expected = test
    actual = remove_smallest(number, original)
    assert actual == expected, "Wrong :("
    assert actual is not original, "You can't change original list"
'''                                    

songs_db = [ {
 'artist': 'Led Zeppelin', 
 'title': 'Stairways to heaven', 
 'playback': '09:20' 
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
 'playback': '02:20' 
}
]

'''
def get_song(db, len_seconds):
    # ...
    #return "Best possible song: {}/{}".format(db[-1]['artist'],db[-1]['title'])
    minute=len_seconds/60
    timeer='0{}:00'.format(str(round(minute)))
    for songs in songs_db:
        if timeer >= songs['playback']:
            return songs['title']
        else:
            return False 

           
    
print(get_song(songs_db, 145))

'''
from collections import defaultdict
test_list = ["tsar", "rat", "tar", "star", "tars", "cheese"]

def group_anagrams(test_list):
    temp=defaultdict(test_list)
    for ele in test_list:
        temp[str(sorted(ele))].append(ele)
    print(list(temp.values()))    

print(group_anagrams(test_list))
                                    
