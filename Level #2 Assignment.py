#Nathan Nielson
#Level #2 Assignment

#Prints Header for the Road Trip Planner
print("\n================================", \
    "\n\tROAD TRIP PLANNER", \
    "\n================================\n"
)

""" Asks for:
• User’s name
• Destination
• One-way distance in miles
• Vehicle miles per gallon
• Gas price per gallon
• Number of travelers
"""
s_user_name = input("What is your name? ")
s_destination = input("Where are you going? ")
i_one_way_distance = int(input("How many miles is the one-way trip? "))
i_miles_per_gallon = int(input("What is your vehicle's miles per gallon? "))
f_gas_pricep_per_gallon = float(input("What is the gas price per gallon? "))
i_number_of_travelers = int(input("How many travelers are going? "))

""" Calculates:
• total miles from one-way distance
• gallons needed as float using total miles and mpg
• Converts number of gallons needed into integer (rounding up)
• total gas cost from gallons needed from gallons needed and price per gallon
• cost per traveler using total gas cost and number of travelers
"""
i_total_miles = i_one_way_distance * 2
f_gallons_needed = i_total_miles / i_miles_per_gallon
i_gallons_needed = int(f_gallons_needed)
f_total_gas_cost = i_gallons_needed * f_gas_pricep_per_gallon
f_cost_per_traveler = f_total_gas_cost / i_number_of_travelers

""" Prints trip summary including:
• The traveler’s name & destination
• The gallons needed
• The price per gallon
• The total gas cost
• The # of travelers
• The cost per traveler
"""
print(f"\n================================ \
    \n\t{s_user_name.upper()}'S {s_destination.upper()} TRIP \
    \n================================ \
    \
    \n\nTotal Gallons Needed: {i_gallons_needed} \
    \nGas Price: ${f_gas_pricep_per_gallon} \
    \
    \n\nTotal Cost of Gas: ${f_total_gas_cost:.2f} \
    \
    \n\nTotal Travelers: {i_number_of_travelers} \
    \nCost Per Traveler: ${f_cost_per_traveler:.2f} \
    \
    \n\n================================ \
    \n\tHave a safe trip!\n\n"
)
