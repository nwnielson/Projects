some_rando_list = []

some_rando_list.append("blah")

print(some_rando_list)

some_rando_list.extend(["yadda", "hello", "ahoy"])

# Removes the last index (can specify which one you want to pop though)
some_rando_list.pop()

# Removes the first instance of a certain value
some_rando_list.remove("hello")

# Can insert things at certain index
some_rando_list.insert(0, "oh hi")

# Counts how many times a certain value appears in the list
print(some_rando_list.count("blah"))

# Checks if certain value is contained in the list.
if "yadda" in some_rando_list :
    print("Found the word!")

print(some_rando_list)
