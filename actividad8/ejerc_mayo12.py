
list1=[]
list2=[]
for i in range(20):
    user= int(input('Digite 10 números: '))
    if user %2==0:
        list1.append(user)
    if user%2!=0:
        list2.append(user)

print (list1, list2)      