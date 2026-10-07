#Heaven Neumann
#Project 1

def printMenu():
    print()
    print("~MENU~")
    print("    a) Test task 1, Compound Interest Calculator")
    print("    b) Test task 2, Number Swapping / Quotient and Remainder")
    print("    c) Test task 3, BMI Calculator")
    print("    q) Quit")

printMenu()
menuChoice = input("What will it be: ")

while menuChoice != "q":
    match menuChoice:
        case "a":
            while True:
                print()
                print("Let's calculate the compound interest")
                PV = float(input("Please enter how much you wish to invest: "))
                INT = float(input("What is the interest rate: "))
                YRS =int(input("In years, how long are you investing for: "))
                FV = PV*((1+(INT/100))**YRS)
                print(f"Your investment will grow to ${FV:.2f} after {YRS} years(s) at the rate of {INT}")
                print()
                print("Do you want to test more values:")
                print("    yes, Test more values")
                print("    no, Go to menu")
                more = input("Enter 'yes' or 'no': ")
                if more != "yes" and more != "no":
                    while more != "yes" and more != "no":
                        more = input("!Invalid! Enter 'yes' or 'no': ")
                elif more == "yes":
                    continue
                else:
                    printMenu()
                    menuChoice = input("What will it be: ")
                    break
            '''
            ~MENU~
                a) Test task 1, Compound Interest Calculator
                b) Test task 2, Number Swapping / Quotient and Remainder
                c) Test task 3, BMI Calculator
                q) Quit
            What will it be: a

            Let's calculate the compound interest
            Please enter how much you wish to invest: 1000.0
            What is the interest rate: 5.0
            In years, how long are you investing for: 30
            Your investment will grow to $4321.94 after 30 years(s) at the rate of 5.0

            Do you want to test more values:
                yes, Test more values
                no, Go to menu
            Enter 'yes' or 'no': yes

            Let's calculate the compound interest
            Please enter how much you wish to invest: 1530.50
            What is the interest rate: 5.0
            In years, how long are you investing for: 15
            Your investment will grow to $3181.80 after 15 years(s) at the rate of 5.0

            Do you want to test more values:
                yes, Test more values
                no, Go to menu
            Enter 'yes' or 'no': yes

            Let's calculate the compound interest
            Please enter how much you wish to invest: 1000000
            What is the interest rate: 1.5
            In years, how long are you investing for: 5
            Your investment will grow to $1077284.00 after 5 years(s) at the rate of 1.5

            Do you want to test more values:
                yes, Test more values
                no, Go to menu
            Enter 'yes' or 'no': yes

            Let's calculate the compound interest
            Please enter how much you wish to invest: 0.93
            What is the interest rate: 2.25
            In years, how long are you investing for: 1000
            Your investment will grow to $4283508449.71 after 1000 years(s) at the rate of 2.25

            Do you want to test more values:
                yes, Test more values
                no, Go to menu
            Enter 'yes' or 'no': 
            '''


        case "b":
            while True:
                print()
                num1 , num2 = input("Enter 2 numbers, separated by a space: ").split()
                print(f"The two numbers you entered {num1} {num2}")
                temp = int(num1)
                num1 = int(num2)
                num2 = temp
                print(f"Your two numbers after swapping  {num1} {num2}")
                quotient = int(num1 / num2)
                remainder = int(num1 % num2)
                print(f"The quotient when {num1}/{num2} is: {quotient}")
                print(f"The remainder when {num1} is divided by {num2} is: {remainder}")

                print()
                print("Do you want to test more values: ")
                print("    yes, Test more values")
                print("    no, Go to menu")
                more = input("Enter 'yes' or 'no': ")
                if more != "yes" and more != "no":
                    while more != "yes" and more != "no":
                        more = input("!Invalid! Enter 'yes' or 'no': ")
                elif more == "yes":
                    continue
                else:
                    printMenu()
                    menuChoice = input("What will it be: ")
                    break

            '''
            ~MENU~
                a) Test task 1, Compound Interest Calculator
                b) Test task 2, Number Swapping / Quotient and Remainder
                c) Test task 3, BMI Calculator
                q) Quit
            What will it be: b

            Enter 2 numbers, separated by a space: 12 35
            The two numbers you entered 12 35
            Your two numbers after swapping  35 12
            The quotient when 35/12 is: 2
            The remainder when 35 is divided by 12 is: 11

            Do you want to test more values: 
                yes, Test more values
                no, Go to menu
            Enter 'yes' or 'no': yes

            Enter 2 numbers, separated by a space: 35 13
            The two numbers you entered 35 13
            Your two numbers after swapping  13 35
            The quotient when 13/35 is: 0
            The remainder when 13 is divided by 35 is: 13

            Do you want to test more values: 
                yes, Test more values
                no, Go to menu
            Enter 'yes' or 'no': yes

            Enter 2 numbers, separated by a space: 35 0
            The two numbers you entered 35 0
            Your two numbers after swapping  0 35
            The quotient when 0/35 is: 0
            The remainder when 0 is divided by 35 is: 0

            Do you want to test more values: 
                yes, Test more values
                no, Go to menu
            Enter 'yes' or 'no": yes

            Enter 2 numbers, separated by a space: 0 35
            The two numbers you entered 0 35
            Your two numbers after swapping  35 0
            Traceback (most recent call last):
                quotient = int(num1 / num2)
                            ~~~~~^~~~~~
            ZeroDivisionError: division by zero
            '''
        case "c":
            while True:
                print()
                print("Please pick which unit of measurement to use:")
                print("    a) USA Empirical System")
                print("    b) English Metric System")
                unit = input("Please select 'a' of 'b': ")

                if unit != "a" and unit != "b":
                    print("!Invalid! Please select 'a' of 'b'")
                
                    
                elif unit == "a":
                    print()
                    print("You selected 'USA Empirical System'")

                    height = float(input("Please enter you height in inches: "))
                    if height <= 0:
                        while height <= 0:
                            print("You have entered an unsupported value for height")
                            height = float(input("Please enter a supported value: "))

                    weight = float(input("Please enter you weight in pounds: "))
                    if weight < 0:
                        while weight < 0:
                            print("You have entered an unsupported value for weight")
                            weight = float(input("Please enter a supported value: "))

                    BMI = 703 * (weight / height ** 2)

                    if BMI < 18.5:
                        print(f"Your BMI is {BMI:.2f}, you are underweight")
                    elif BMI < 25.0:
                        print(f"Your BMI is {BMI:.2f}, you are within a normal range")
                    else:
                        print(f"Your BMI is {BMI:.2f}, you are overweight")

                    print()
                    print("Do you want to test more values: ")
                    print("    yes, Test more values")
                    print("    no, Go to menu")
                    more = input("Enter 'yes' or 'no': ")
                    if more != "yes" and more != "no":
                        while more != "yes" and more != "no":
                            more = input("!Invalid! Enter 'yes' or 'no': ")
                    elif more == "yes":
                        continue
                    else:
                        printMenu()
                        menuChoice = input("What will it be: ")
                        break

                else:
                    print()
                    print("You selected 'English Metric System'")
                    height = float(input("Please enter your height in meters: "))
                    if height <= 0:
                        while height <= 0:
                            print("You have entered an unsupported value for height")
                            height = float(input("Please enter a supported value: "))

                    weight = float(input("Please enter you weight in kilograms: "))
                    if weight < 0:
                        while weight < 0:
                            print("You have entered an unsupported value for weight")
                            weight = float(input("Please enter a supported value"))

                    BMI = weight / height ** 2

                    if BMI < 18.5:
                        print(f"Your BMI is {BMI:.2f}, you are underweight")
                    elif BMI < 25.0:
                        print(f"Your BMI is {BMI:.2f}, you are within a normal range")
                    else:
                        print(f"Your BMI is {BMI:.2f}, you are overweight")

                    print()
                    print("Do you want to test more values: ")
                    print("    yes, Test more values")
                    print("    no, Go to menu")
                    more = input("Enter 'yes' or 'no': ")
                    if more != "yes" and more != "no":
                        while more != "yes" and more != "no":
                            more = input("!Invalid! Enter 'yes' or 'no': ")
                    elif more == "yes":
                        continue
                    else:
                        printMenu()
                        menuChoice = input("What will it be: ")
                        break
            '''
            ~MENU~
                a) Test task 1, Compound Interest Calculator
                b) Test task 2, Number Swapping / Quotient and Remainder
                c) Test task 3, BMI Calculator
                q) Quit
            What will it be: c

            Please pick which unit of measurement to use:
                a) USA Empirical System
                b) English Metric System
            Please select 'a' of 'b': a

            You selected 'USA Empirical System'
            Please enter you height in inches: 0
            You have entered an unsupported value for height
            Please enter a supported value: 59
            Please enter you weight in pounds: -50
            You have entered an unsupported value for weight
            Please enter a supported value: 0
            Your BMI is 0.0, you are underweight

            Do you want to test more values: 
                yes, Test more values
                no, Go to menu
            Enter 'yes' or 'no': yes

            Please pick which unit of measurement to use:
                a) USA Empirical System
                b) English Metric System
            Please select 'a' of 'b': a

            You selected 'USA Empirical System'
            Please enter you height in inches: 59
            Please enter you weight in pounds: 90
            Your BMI is 18.18, you are underweight

            Do you want to test more values: 
                yes, Test more values
                no, Go to menu
            Enter 'yes' or 'no': yes

            Please pick which unit of measurement to use:
                a) USA Empirical System
                b) English Metric System
            Please select 'a' of 'b': a

            You selected 'USA Empirical System'
            Please enter you height in inches: 61
            Please enter you weight in pounds: 110
            Your BMI is 20.78, you are within a normal range

            Do you want to test more values: 
                yes, Test more values
                no, Go to menu
            Enter 'yes' or 'no': yes

            Please pick which unit of measurement to use:
                a) USA Empirical System
                b) English Metric System
            Please select 'a' of 'b': a

            You selected 'USA Empirical System'
            Please enter you height in inches: 67
            Please enter you weight in pounds: 190
            Your BMI is 29.75, you are overweight

            Do you want to test more values: 
                yes, Test more values
                no, Go to menu
            Enter 'yes' or 'no': yes

            Please pick which unit of measurement to use:
                a) USA Empirical System
                b) English Metric System
            Please select 'a' of 'b': a

            You selected 'USA Empirical System'
            Please enter you height in inches: 67.5
            Please enter you weight in pounds: 190.9
            Your BMI is 29.45, you are overweight

            Do you want to test more values: 
                yes, Test more values
                no, Go to menu
            Enter 'yes' or 'no': yes

            Please pick which unit of measurement to use:
                a) USA Empirical System
                b) English Metric System
            Please select 'a' of 'b': w
            !Invalid! Please select 'a' of 'b'

            Please pick which unit of measurement to use:
                a) USA Empirical System
                b) English Metric System
            Please select 'a' of 'b': b

            You selected 'English Metric System'
            Please enter your height in meters: 2.006
            Please enter you weight in kilograms: 64
            Your BMI is 15.90, you are underweight

            Do you want to test more values: 
                yes, Test more values
                no, Go to menu
            Enter 'yes' or 'no': yes

            Please pick which unit of measurement to use:
                a) USA Empirical System
                b) English Metric System
            Please select 'a' of 'b': b

            You selected 'English Metric System'
            Please enter your height in meters: 1.72
            Please enter you weight in kilograms: 68
            Your BMI is 22.99, you are within a normal range

            Do you want to test more values: 
                yes, Test more values
                no, Go to menu
            Enter 'yes' or 'no': yes

            Please pick which unit of measurement to use:
                a) USA Empirical System
                b) English Metric System
            Please select 'a' of 'b': b

            You selected 'English Metric System'
            Please enter your height in meters: 1.52 
            Please enter you weight in kilograms: 100
            Your BMI is 43.28, you are overweight

            Do you want to test more values: 
                yes, Test more values
                no, Go to menu
            Enter 'yes' or 'no': no
            '''
        case "q":
            print("Exiting program")
            break
            
           # ~MENU~
           #     a) Test task 1, Compound Interest Calculator
           #     b) Test task 2, Number Swapping / Quotient and Remainder
           #     c) Test task 3, BMI Calculator
           #     q) Quit
           # What will it be: q
           # PS C:\Users\merma\OneDrive\Python> 
        
        case default:
            print("Error: Your choice is not supported")
            printMenu()
            menuChoice = input("What will it be: ")
            '''
            ~MENU~
                a) Test task 1, Compound Interest Calculator
                b) Test task 2, Number Swapping / Quotient and Remainder
                c) Test task 3, BMI Calculator
                q) Quit
            What will it be: w
            Error: Your choice is not supported

            ~MENU~
                a) Test task 1, Compound Interest Calculator
                b) Test task 2, Number Swapping / Quotient and Remainder
                c) Test task 3, BMI Calculator
                q) Quit
            What will it be: 
            '''
