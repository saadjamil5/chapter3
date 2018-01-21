list=[]
user=''
while user != 'quit':
    toppings=input("Please enter toppings:")
    if toppings =='quit':
      break
    else:
      list.append(toppings)
input("You added")
print(list)