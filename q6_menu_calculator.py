print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice = int(input("Enter choice: "))
a = int(input("Enter two numbers: "))
b = int(input())
if choice == 1:
    print(f"Sum = {a + b}")
elif choice == 2:
    print(f"Difference = {a - b}")
elif choice == 3:
    print(f"Product = {a * b}")
elif choice == 4:
    if b != 0:
        print(f"Quotient = {a / b}")
    else:
        print("Cannot divide by zero")
else:
    print("Invalid choice")