import math 
def calculator(num1,num2):
    '''thiss is a documention string when i use __doc__ this multiline printed as output uiciuqic;i'''
    print("----------This is Calc Function from calculator-------------")
    print("Addition : " , num1+num2)
    print("Substraction : ",abs(num1-num2))
    print("Multiplication :",num1 * num2)
    print("Division :",num1/num2)
    print("Floor Division :",num1 // num2)
    print("Exponential for val1(10):",math.pow(num1,2))
    print("Exponential for val2(5):",math.pow(num2,2))
    print("Square root for val1(10):",math.sqrt(num1))
    print("Square root for val2(5):",math.sqrt(num2))
    

employee = {
    "name" : "siva",
    "Desingantion" : "intern"
}

class C:
    pass 

print(C.__module__)

if __name__ == "__main__" :
    print("this is main method")