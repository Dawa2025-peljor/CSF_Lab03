numbers = [2, 4, 6, 8, 10]
print("List: 2 4 6 8 10")
search = int(input("Searching for: "))
found = False
for num in numbers:
    if num == search:
        found = True
        break
if found:
    print("Number found")
else:
    print("Number not found")