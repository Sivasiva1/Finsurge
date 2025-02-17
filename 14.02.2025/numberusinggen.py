arr1 = []  # Even numbers
arr2 = []  # Odd numbers
arr3 = []  # Greater than 100
arr4 = []  # Less than or equal to 100

def generator(left,right):
    while left <= right:
        yield left*5 
        left += 1 
def calculation():
 for i in generator(1,100):
    ans = i 
    if ans % 2 == 0:
        arr1.append(ans) 
    else:
        arr2.append(ans)
    if ans >=100: 
        arr3.append(ans)
    else:
        arr4.append(ans)
def details():
    
    print("Even numbers: " , arr1)
    print(" Odd numbers" ,arr2)
    print("Greater than 100 ",arr3)
    print("Less than 100 ",arr4)
    
calculation()
details() 