def add(x, y):
    return x + y 
def subtraction(x, y):
    return x - y
def multiplication(x, y):
    return x * y
def division(x, y):
    return x / y

num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))

print("Operation Selection")
print("1. addition")
print("2. substitution")
print("3. multiplication")
print("4. division")

while True: 

    choice = int (input ("Enter a choice from the selection above: "))
    
    if choice == 1:
        print( num1, "+", num2, "=", add(num1, num2))
    elif choice == 2:
        print(num1, "-", num2, "=", subtraction(num1, num2))
    elif choice == 3:
        print(num1, "*", num2, "=", multiplication(num1, num2))
    elif choice == 4:
        print(num1, "/", num2, "=", division(num1, num2))
    break
else: 
    print("Invalid choice")
