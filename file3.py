#Get input from the user
char = input("enter a character: ")

# check if the character is an alphabet
if len(char) == 1: #ensure only one character is entered
    if char.isalpha():
        print(f"'{char}' is an alphabet.")
    else:
        print(f"'{char}' is not an alphabet.")
else:
    print("please enter only one character.")            