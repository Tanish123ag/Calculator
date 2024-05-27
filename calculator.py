print("1)Add")
print("2)Subtract")
print("3)Multiply")
print("4)Division")
print("5)Float division")
print("6)Factorial")
print("7)Power")

def add():
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the second number:"))
    print("The solution is : "+str(int(num1)+int(num2)))
def subtract():
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the second number:"))
    print("The solution is : "+str(int(num1)-int(num2)))
def multiply():
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the second number:"))
    print("The solution is : "+str(int(num1)*int(num2)))
def division():
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the second number:"))
    print("The solution is : "+str(int(num1)/int(num2)))
def float_division():
    num1=float(input("Enter the first float number:"))
    num2=float(input("Enter the second float number:"))
    print("The solution is:"+str(float(num1)/float(num2)))
def factorial():
    num1=int(input("Enter the number to factorial:"))
    import math
    print("The solution is:"+str(int(math.factorial(num1))))
def power():
    import math
    num1=input("Enter the first number:")
    num2=input("Enter the second number:")
    print("The solution is:"+str(math.pow(int(num1),int(num2))))
option=input("Enter the the operation:")
if option=="1":
    add()
elif option=="2":
    subtract()
elif option=="3":
    multiply()
elif option=="4":
    division()
elif option=="5":
    float_division()
elif option=="6":
    factorial()
elif option=="7":
    power()
else:
    print("Invalid Operation")