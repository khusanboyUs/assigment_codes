friends=['John','Murat','Karma','Hassan']
last_seen=[1,2,7,6]

result={
    friends[i]:last_seen[i]
    for i in range(len(friends))
}

result2=dict(zip(friends,last_seen))

print(result2)