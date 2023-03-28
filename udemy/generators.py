def my_gen():
    counter=0
    while counter <20:
        yield counter
        counter+=1

gen=my_gen()
        
        
def prime_generator(bound):
    for i in bound:
        for n in range(2,i):
            if i%n==0:
                print(f'{i} is not prime')
                break
        else:
            print(f'{i} is the prime')    

#runner=prime_generator(bound=list(gen))
#print(runner)

def find_prime():
    for i in range(0,20):
        for n in range(2,i):
            if i%n==0:
                print('Not prime')
                break
        else:
            print(f"{i} is the prime")


#d=find_prime()
#print(d)
# 
# 
# 
def prime_generator(bound):
    for n in range(2, bound):   # n starts from 2 to bound
        for x in range(2, n):   # check if there is a number x (1<x<n) that can divide n
            if n % x == 0:  # as long as we can find any such x, then n is not prime
                break
        else:   # if no such x is found after exhausting all 1<x<n
            yield n     # generate this prime                    
   
   
class HundredNumbersGenerator:
    def __init__(self):
        self.number=0

    def __next__(self):
        if self.number < 100:
            current=self.number
            self.number+=1
            return current
        else:
            raise StopIteration

    def __iter__(self):
        return self
    


