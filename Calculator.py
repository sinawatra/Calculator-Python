def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        return "ERROR: Division By Zero 555!!"
    return x/y
print("Welcome to Python Calculator!!!!!!")
print("Select Operation: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1,2,3,4): ")
if choice not in ['1','2','3','4']:
    print("Invalid choice")
else:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second numberL: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    if choice == '2':
        print("Result: ", subtract(num1,num2))
    if choice == '3':
        print("Result", multiply(num1, num2))
    if choice =='4':
        print("Result: ", divide(num1, num2))