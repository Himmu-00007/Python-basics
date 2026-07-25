def main():
    print("Welcome to the Essay Writing Program! 😊")

    continue_choice = input("Do you want to continue? (Y/N) 🤔 ").strip().upper()
    if continue_choice != "Y":
        print("Okay, goodbye 😊")
        print("Press alt+F4 to exit 👍")
        return
name = input("What's your name? 🧐 ").strip()
gender = input("What's your gender? (M/F) 🧐 ").strip().upper()
    title = "Sir ♂️" if gender == "M" else "Madam ♀️"
       essay = input("Write an essay on the topic of 'National Pride' 😊: ")
    length = len(essay)
    print(f"Length of this essay is: {length}")

    show_half = input("Want the half of the essay? (Y/N) 🧐 ").strip().upper()
    half_essay = essay[:length // 2]

    if show_half == "Y":
        print(half_essay)
    else:
        print(f"Understood, {title}!")

    print(f"Thank you for your time, {title}, {name}!")
    print("Press alt+F4 to exit 👍")


