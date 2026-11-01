a = input ("First number : ")
b = input("Second number : ")
c = input("Choose (+ - * /) : ")
a = int (a)
b = int(b)
def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b == 0:
        return "Cannot divide by zero"
    else:
        return a/b
if c == "+":
    print("result : ",add(a,b))
elif c == "-":
    print("result : ",subtract(a,b))
elif c == "*":
    print("result : ",multiply(a,b))
elif c == "/":
    print("result : ",divide(a,b))

#Pro verison 
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


while True:
    a = int(input("First number: "))
    b = int(input("Second number: "))
    c = input("Choose (+ - * /): ")

    if c == "+":
        result = add(a, b)
    elif c == "-":
        result = subtract(a, b)
    elif c == "*":
        result = multiply(a, b)
    elif c == "/":
        result = divide(a, b)
    else:
        result = "Invalid operator"

    print("Result:", result)

    again = input("Do you want to continue? (yes/no): ")
    if again.lower() != "yes":
        break

