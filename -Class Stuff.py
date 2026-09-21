"""Functions"""
#Give it numbers, and it will give tell you if they're positive or negative, 
#and keeps track of how many positive, negative, and zeros there are
def positive_or_negative(numbers) :
    positive_number_count = 0
    negative_number_count = 0
    zero_number_count = 0

    #loop
    for index, int in enumerate(numbers) :
        #checks if number is bigger than 0, if so, prints that it's positive and increases positive_number_count +=1
        if numbers[index] > 0 :
            print(str(numbers[index]) + " is positive")
            positive_number_count += 1


        #checks if number is less than 0, if so, prints that it's positive and increases negative_number_count +=1
        if numbers[index] < 0 :
            print(str(numbers[index]) + " is negative")
            negative_number_count += 1

        #checks if number is 0, if so, prints that it's positive and increases zero_number_count +=1
        if numbers[index] == 0 :
            print(str(numbers[index]) + " is equal to 0")
            zero_number_count += 1

    print("\n # of positive numbers: " + str(positive_number_count), "\n", \
        "# of negative numbers: " + str(negative_number_count), "\n", \
        "# of zeros: " + str(zero_number_count))
    return





"""Calls"""
positive_or_negative([5, 10, -7, 4, -17, 0])
