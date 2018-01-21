motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0]='ducati'
print(motorcycles)


motorcycles1=['honda','yamaha','suzuki']
print(motorcycles)
motorcycles1.append('ducati')
print(motorcycles1)

motorcycles2=[]
motorcycles2.append('honda')
motorcycles2.append('suzuki')
motorcycles2.append('Nissan')
print(motorcycles2)



motorcycles3=['honda','yamaha','suzuki']
motorcycles3.insert(0,'Toyota')
print(motorcycles3)

motorcycles4=['honda','yamaha','suzuki']
print(motorcycles4)
del motorcycles4[1]
print(motorcycles4)


motorcycles5=['honda','yamaha','suzuki']
print(motorcycles5)
popped_motorcycles5=motorcycles5.pop()
print(motorcycles5)
print(popped_motorcycles5)


motorcycles6=['honda','yamaha','suzuki']
Last_owned=motorcycles6.pop()
print("The last motorcycle I owned was a"+" "+Last_owned.title()+".")


motorcycles7=['honda','yamaha','suzuki']
first_owned=motorcycles7.pop(1)
print("The first motorcycle I owned was a"+" "+first_owned.title()+".")

motorcycles8=['honda','yamaha','suzuki']
print(motorcycles8)
motorcycles8.remove('suzuki')
print(motorcycles8)


motorcycles9=['honda','yamaha','suzuki']
print(motorcycles9)
too_expensive='suzuki'
motorcycles9.remove(too_expensive)
print(motorcycles9)
print("A"+" "+too_expensive.title()+" "+"is too expensive for me.")
