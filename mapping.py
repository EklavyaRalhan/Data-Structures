list1 = [1,2,3,4]
print(list1)
list2 = [5,6,7,8]
print(list2)
list3 = map(lambda n,y: n+y, list2,list1)

newlist = (list(list3))
list4 = map(lambda x: x*x, newlist)
print(list(list4))