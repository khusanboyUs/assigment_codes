user=input("Please enter your friend's name seperating them with comma: ").split(',')

friends_file=open('friends.txt','r')
friends_list=[names.strip() for names in friends_file.readlines()]
friends_file.close()

nearby_friends_set=set(friends_list)
friends_set=set(user)

all_friends=nearby_friends_set.intersection(friends_set)
saved_friends=open("friend_n.txt","w")

for indx,friends in enumerate(all_friends,start=1):
    print(f'{friends,indx} is here')
    if indx < len(all_friends):
        saved_friends.write(f'{friends}\n')
    elif indx == len(all_friends):
        saved_friends.write(f'{friends}')
     
      

saved_friends.close()    


import json