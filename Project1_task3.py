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