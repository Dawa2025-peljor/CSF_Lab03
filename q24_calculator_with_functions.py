def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "Cannot divide by zero"

while True:
    print("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
    choice = int(input("Enter choice: "))
    if choice == 5:
        break
    if choice in (1, 2, 3, 4):
        a = int(input("Enter two numbers: "))
        b = int(input())
        if choice == 1:
            print(f"Sum = {add(a, b)}")
        elif choice == 2:
            print(f"Difference = {subtract(a, b)}")
        elif choice == 3:
            print(f"Product = {multiply(a, b)}")
        elif choice == 4:
            print(f"Quotient = {divide(a, b)}")
    else:
        print("Invalid choice")