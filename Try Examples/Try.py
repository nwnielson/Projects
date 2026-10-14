has_error = True

while has_error:
    try:
        number = int(input("Enter a number: "))
        print(number)
    
    except ValueError:
        print("Invalid number. Please try again. ")
        continue
    except KeyboardInterrupt :
        print("You stopped the program.")
    except :
        print("You got some rando error.")
        break
    else : 
        has_error = False
        continue
    finally :
        print("Got through it! ")
    