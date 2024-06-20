n1 = float(input("Enter 1st number: "))
n2 = float(input("Enter 2st number: "))

def calculator(n1,n2):

    print("\n Enter 1 for Addition \n Enter 2 for Substraction \n Enter 3 for Multiplication \n Enter 4 for Division")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print(n1+n2)
    elif choice == 2:
        print(n1-n2)
    elif choice == 3:
        print(n1*n2)
    elif choice == 4:
        if n2 == 0:
            print("Division by zero not possible.")
        print(n1/n2)
    else:
        print("Invalid input.")
        calculator(n1,n2)
        
calculator(n1,n2)
