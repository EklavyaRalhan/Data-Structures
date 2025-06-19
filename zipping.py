list1 = [3,6,9,12]
list2 = [5,10,15,20]

list3 = zip(list1,list2)
print(list(list3))

list4 = [6,12,18,24]
list5 = [7,14,21,28]
list6 = zip(list4,list5[::-1])
print(list(list6))

item = ['watch', 'phone', 'laptop']
price = [100, 300, 700]

dic1 = {item:price for item, price in zip(item,price)}
print(dic1)