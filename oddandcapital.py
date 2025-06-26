numbers = int(input("Enter Numbers"))
number = []
number.append(numbers)

odd = [x for x in number if x%2 != 0]
print("List of odd numbers: ", odd)


fruits = ['apple', 'banana', 'cherry']
newfruits = [item.capitalize() for item in fruits]
print(newfruits)