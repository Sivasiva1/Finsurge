def fibbo():
    n1 = 0
    n2 = 1
    print(n1,n2,end=" ")
    for i in range(1,10):
        n3 = n1 + n2 
        print(n3,end=" ")
        n1 = n2 
        n2 = n3 
    print()
def factorial(n):
    factorial = 1 

    for i in range(1,fact+1):
        factorial*=i 
    print(factorial)
def reversenum(num):

    temp = num 
    summ = 0 
    while temp > 0:
        digit = temp % 10 
        summ = summ * 10 + digit
        temp = temp // 10 
    print(summ)
def reversearr(arr):
    left = 0
    right = len(arr)-1

    while left <right:
        temp  =arr[left]
        arr[left] = arr[right]
        arr[right] = temp 
        left+=1
        right-=1 
    print(arr)
def pallindrome(s):
    new = ""

    for i in s:
        new = i + new 
    if new ==  s:
        print("pallindorme")
    else:
        print("not pallindrome")
if __name__=="__main__":
    while True:
        number = int(input("Enter the number :"))
        if number == 1:
         print("Fibbonnacci Series")
         fibbo()

        elif number == 2:
            print("Factorial of number")
            fact = int(input("enter the factorial "))
            factorial(fact)
        elif number == 3:
            print("reverse of number")
            num = int(input("Enter the number : "))
            reversenum(num)
        elif number == 4:
            print("Reverse of array :")

            arr = list(map(int, input("Enter numbers for array: ").split()))

            reversearr(arr)
        elif number == 5:
            print("pallindrome of a string")
            string = str(input("Enter the string "))
            pallindrome(string)
        else:
            print(" Invalid input ")