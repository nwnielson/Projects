#Take in inputs for first name, last name, birth year, street address, city, state, and calculates age in 2020.
sFirst_Name = input("What is your first name?")
sLast_Name = input("What is your last name?")
iBirth_Year = int(input("What is your birthyear?"))
i2020_Age = 2020 - iBirth_Year
sStreet_Address = input("What is your street address?")
sCity = input("What city do you live in?")
sState = input("What state do you live in?").upper()

#prints information in following format:
#First_Name Last_Name (Both uppercase)
#Street_Address
#City State (State upper case)
#In 2020, "First_Name" was "Age in 2020" years old.
print(sFirst_Name.upper() + " " +sLast_Name.upper(), \
       "\n", sStreet_Address, \
       "\n", sCity + " " + sState, \
       "\nIn 2020, " + sFirst_Name + " was " + str(i2020_Age) + " years old.")