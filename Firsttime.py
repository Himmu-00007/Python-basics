def main():
    print("Welcome to the Essay Writing Program! 😊")

    continue_choice = input("Do you want to continue? (Y/N) 🤔 ").strip().upper()
    if continue_choice != "Y":
        print("Okay, goodbye 😊")
        print("Press alt+F4 to exit 👍")
        return
B = input("Do you want to continue? (Y/N)🤔 ")
if B == "Y":
    O = input("What's your name?🧐 ")
    A = input("What's your gender?(M/F)🧐 ")
    if A == "M":
        S = "Sir"+"♂️"
    else:
        S = "Madam"+"♀️"
    E = input("Write an essay on the topic of 'National Pride'😊: ")
    length = len(E)
    print("                                                                 Length of this essay is:", length)
    X = input("Want the half of the essay?(Y/N)🧐 ")
    P = E[0:length//2]
    if X == "Y":
        print(P)
    else:
        print("                                                                     Understood,", S + "!")
    print("Thank you for your time, " + S + ", " + O + "!")

