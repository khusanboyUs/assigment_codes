friends=['John','Julia','Anna','Filip','Adrian']
guests=['Adam','Julia','Hanna','Andrzej','Tomasz']

friends2=set([friend.lower() for friend in friends])
guests3=set([guest.lower() for guest in guests])

print(friends2.intersection(guests3))