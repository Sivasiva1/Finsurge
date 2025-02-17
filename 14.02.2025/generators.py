def generator(): #this is a generator function bcoz of the 'yield' 
    print("one")
    yield 1 
    print("two")
    yield 2 
    print("three")
    yield 3
    print("four")
    yield 4 
g = generator()

while True:
  try:
    print(next(g)) 
  except StopIteration as e:
     break 

#generator function using for loop  
def gen(l,r):
   
   while l <= r:
      yield l 
      l += 1

for i in gen(1,5):
    print(i*i) 

#Generator Expression

ans = (x*x for x in range(1,6) if i % 2==0)
for i in ans:
   print(i)


'''generator : Type of iterator '''
'''yield : pause the exceution and used return sequence of values  '''
