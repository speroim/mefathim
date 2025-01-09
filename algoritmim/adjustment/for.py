myList = [x for x in range (1,11) if x%2==0]
print(myList)

myList = [x for x in "word"]
print(myList)

myList = [x if x%2==0 else "odd" for x in range(0,11)]
print(myList)