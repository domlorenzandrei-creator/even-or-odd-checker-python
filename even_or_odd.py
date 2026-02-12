def title():
        print("Even or Odd Checker")


title()

while True:
    try:
        num = int(input("Enter a number (1-100): "))
        if num < 1 or num > 100:
            print("Please enter a number between 1-100.")
        elif num % 2 == 0:
            print("The number is even.")
        else:
            print("The number is Odd")


    except ValueError:
        print("Please enter a valid number.")
        break
