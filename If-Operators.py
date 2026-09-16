f_calculation = 10 / 3
#Calculation below is how you round something up
i_calculation = -(-f_calculation // 1)

comparison1 = ((5>3) and (3==4)) or ((2>3) and (4>2))

#print(comparison1)
print(f"The result is:  {i_calculation}")

age = int(input("Enter your age: \n"))

if age >= 40:
    weight = int(input("Enter your weight: "))
    if weight >= 200:
        print("\nWow, old and fat are we?")
    elif weight <= 100:
        print("We only use freedom units here.")
    else:
        print("You're old, but you seem healthy enough.")
elif age < 0:
    print("Shouldn't you be in the womb right now?")
else:
    print("Shouldn't you be in school right now?")