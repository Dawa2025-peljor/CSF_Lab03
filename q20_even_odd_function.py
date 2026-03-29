def even_odd(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"

num = int(input("Enter number: "))
print(f"The number is {even_odd(num)}")