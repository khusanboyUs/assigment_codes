for i in range(2,100):
    for n in range(2,i):
        if i%n==0:
            print(f" {i} equals to {n} * {i//n}")
            break 
    else:
        print(f" {i} is prime")       