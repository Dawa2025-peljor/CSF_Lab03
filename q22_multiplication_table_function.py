def print_table(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

n = int(input("Enter number: "))
print_table(n)
