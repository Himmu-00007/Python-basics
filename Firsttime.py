A=input("What's your gender?(M/F) ")
if A=="M":
    S="Sir"
else:
    S="Madam"
E=input("Write an essay on the topic of 'National Pride': ")
length=len(E)
print("                                                                 Length of this essay is:", length)
X=input("Want the half of the essay?(Y/N)")
P=E[0:length//2]
if X=="Y":
    print(P)
else:
    print("                                                                     Understood,", S+"!")


