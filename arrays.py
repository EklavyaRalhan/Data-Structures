import array as arr
elements = arr.array('i',[1, 3, 5, 3, 7, 9, 3])

array2 = [1, 3, 5, 3, 7, 9, 3]
print(elements)

print("Number of 3s in the array is ", elements.count(3))

array2.reverse()
print(array2)