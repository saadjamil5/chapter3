print("Ex:3-4")
Invitation=['Oj','Arbaz','Saad']
print(Invitation[0]+" "+"comes on dinner tonight")
print(Invitation[1]+" "+"Comes on Dinner tonight")
print(Invitation[2]+" "+"Comes on Dinner tonight")

print("Ex:3-5")
Guestlist3=['Ali','Rafay','Obaid']
print(Guestlist3[0]+" "+"comes on dinner tonight")
print(Guestlist3[1]+" "+"Comes on Dinner tonight")
print(Guestlist3[2]+" "+"Comes on Dinner tonight")
print("Ali will not come due to some reason")
Guestlist3.remove('Ali')
Guestlist3.insert(0,'Ahsan')
print(Guestlist3)
print(Guestlist3[0]+" "+"Please Come on dinner")
print(Guestlist3[1]+" "+"Please Come on dinner")
print(Guestlist3[2]+" "+"Please Come on dinner")



print("Ex:3-6")
Guestlist1=['Ali','Rafay','Obaid']
print("Hey people,i found a bigger dinner table so, i invites or other friends")
Guestlist1.insert(0,'Muneeb')
Guestlist1.insert(3,'Furqan')
Guestlist1.insert(5,'Wasay')
print(Guestlist1[0]+" "+"plzz come on dinner tonight")
print(Guestlist1[1]+" "+"plzz come on dinner tonight")
print(Guestlist1[2]+" "+"plzz come on dinner tonight")
print(Guestlist1[3]+" "+"plzz come on dinner tonight")
print(Guestlist1[4]+" "+"plzz come on dinner tonight")
print(Guestlist1[5]+" "+"plzz come on dinner tonight")

print("Ex:3.7")
Guestlists=['Ali','Rafay','Obaid','Muneeb','Wasay','Furqan']
print("I can invite only two people on dinner bcoz table is small so that's why!")
print(Guestlists)
popped_Guestlist=Guestlists.pop(1)
print(popped_Guestlist+" "+"Sorry You are not Invite on dinner")
print(Guestlists)
popped_Guestlist=Guestlists.pop(2)
print(popped_Guestlist+" "+"Sorry You are not Invite on dinner")
print(Guestlists)
popped_Guestlist=Guestlists.pop(3)
print(popped_Guestlist+" "+"Sorry You are not Invite on dinner")
print(Guestlists)
popped_Guestlist=Guestlists.pop(1)
print(popped_Guestlist+" "+"Sorry You are not Invite on dinner")
print(Guestlists)
print(Guestlists[0]+" "+"You are still invited")
print(Guestlists[1]+" "+"You are still invited")
print(Guestlists)
del Guestlists[1]
print(Guestlists)
del Guestlists[0]
print(Guestlists)