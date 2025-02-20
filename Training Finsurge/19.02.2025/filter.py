numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even  = tuple(filter(lambda x : x % 2==0 , numbers)) #implicitly iterate the list 
print(even) 

names  =["siva","mahil","sanjay","bala","sanjeeev"]
specific =list(filter(lambda x : x[0]=="s",names)) 
print(specific) 

students = [
    {"name": "John", "score": 85},
    {"name": "Jane", "score": 72},
    {"name": "Dave", "score": 90},
    {"name": "Emma", "score": 60}
]
good = list(filter(lambda x : x["score"]>=75,students)) 
print(good) 

words = ["123", "Python3","hello", "4567", "890"] 

def digits(string):
        if  not string.isdigit():
            return False
        return True 

digit_str = list(filter(digits,words))   
print(digit_str) 

n = range(1, 50)

def threeandfive(a):
        if a % 3 == 0 and a % 5 ==0:
            return True 
        else:
             return False 
nn = list(filter(threeandfive,n))
print(nn) 

#or

nnn = list(filter(lambda x : x%3==0 and x % 5==0,n))
print(nnn) 