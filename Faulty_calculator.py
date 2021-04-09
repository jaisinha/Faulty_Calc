
a=int(input("Enter the first no.\n"))
b=int(input("Enter the second no.\n"))

print("1 for +")
print("2 for /")
print("3 for *")
print("4 for -")
choice=int(input("Enter the choice "))
if(a==3 and b==4 and choice==1):  #pehle likho na varna GALAT
    print("4")
elif(a==3 and b==4 and choice==2):  #pehle likho na varna 
    print("5")
elif(a==3 and b==4 and choice==3):  #pehle likho na varna 
    print("6")
elif(a==3 and b==4 and choice==4):  #pehle likho na varna 
    print("7")

elif(choice==1):
    print(a+b)
elif(choice==2):
    print(a/b)
elif(choice==3):
    print(a*b)
elif(choice==4):
    print(a-b)

else:
    print("out of range")
