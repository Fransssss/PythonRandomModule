import random

print("\n== Random Module == ")
print("1. Output random number to specified range")
print("2. Output random number between 0 and 1")
print("3. List - [ \"Rock\", \"Paper\", \"Scissors\" ]")
choice = input("choice: ")

while choice != 'e' and choice != 'E':
    if choice == '1':
        print("\n> Random number to specified range")
        start_num = input("Input start number: ")
        if start_num.isdigit():
            finish_num = input("Input a finish number: ")
            if finish_num.isdigit():
                if start_num > finish_num:
                    print("\n[ Finish number has to be bigger than start number ]")
                else:
                    print("Random output: [ {} ]".format(random.randint(int(start_num), int(finish_num))))
            else:
                print("\n[ Invalid input ]")
        else:
            print("\n[ Invalid input ]")

    elif choice == '2':
        print("\n> Random Number Between 0 and 1")
        print("Random output: [ {} ]".format(random.random()))

    elif choice == '3':
        print("\n> Random Choice in List")
        list_range = ["Rock", "Paper", "Scissors"]
        print("Random output: [ {} ]".format(random.choice(list_range)))

    else:
        print("\n[ Invalid choice ]")

    print("\n== Random Module == ")
    print("1. Output random number to specified range")
    print("2. Output random number between 0 and 1")
    print("3. List - [ \"Rock\", \"Paper\", \"Scissors\" ]")
    choice = input("choice: ")

if choice == 'e' or choice == 'E':
    print("\nExit Program")