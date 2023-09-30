import re

# Ask the user to input his (name, age, street, city, and country)


name = input("Enter your name: ")
age = input("Enter your age: ")
street = input("Enter your street: ")
city = input("Enter your city: ")
country = input("Enter your country: ")

# (related to question 1) Print the output on the console, it should look like this:
print('"Name: ' + name + '"')
print('"Age: ' + age + '"')
print('"Address: ' + street + ', ' + city + ', ' + country + '"')

# Calculate the age after 5 years
future_age = int(age) - 5
# Print the desired output with dynamic data
print(f'"Hello {{{name}}} Your age is {future_age} Years Old, Your Address is {street}, {city}, {country}."')

# Print the type of each variable
print(type(name), type(age))
print(type(street), type(city))
print(type(country))
# q5
print(f'"Hello {name}, How Are You? \\" \\"\\"\\" Your Age Is \\"{age}\\" + And Your Country Is: Palestine')

# q6
print(f"""\"Hello '{name}', How Are You? \\
\"\"\" Your Age Is \"15\"\"\" + And
 Your City Is: {city}""")

# q7
name = 'ITF Gsg Python'
# Print_using indexing
print(f"First Letter Is \"{name[0]}\"")
print(f"Third Letter Is \"{name[2]}\"")
print(f"Last Letter Is \"{name[-1]}\"")
# q8
# Print_using slicing
print(name[2:5])
print(name[:3])
print(name[2:6][::-1])
print(name[::-1])

# q9
name = "$&$&Mohammed$&$&"
characters_to_remove = "$&"
new_name = name.strip(characters_to_remove)
print(new_name)
# q10
msg = "I %7 Python And Although I %7 GSG with Zakaria"
new_msg = msg.replace("%7", "Love")
print(new_msg)
# q11\12
num1 = "4"
num2 = "56"
num3 = "963"
num4 = "385"
num5 = "8719"
num6 = "87190"
length = 5
print(num1.zfill(length))
print(num2.zfill(length))
print(num3.zfill(length))
print(num4.zfill(length))
print(num5.zfill(length))
print(num6)

# q 13
string1 = "welcome in python"
result1 = string1.title()
print(result1)
string1 = "welcome in python"
result1 = string1.capitalize()
print(result1)
# q14
first_name = "Dana"
print(f"{'*' * 11}{first_name}")
print(f"{'*' * 11}{first_name}{'*' * 11}")
print(f"{first_name}{'*' * 11}")
# q15
name_one = "SaMER"
name_two = "Abed"
print(name_one[0].lower() + name_one[1:].upper())
print(name_two[0].lower() + name_two[1:].upper())
print(name_one.lower())
print(name_two.upper())
# q16
print(f"Is name_one all uppercase? {first_name.isupper()}")
print(f"Is name_two all lowercase? {first_name.islower()}")

# q17
print(f"Does name_one start with 'S'? {first_name.startswith('S')}")
print(f"Does name_two end with 'HD'? {first_name.endswith('HD')}")
# q18
msg = "I Love Python And Although I Love GSG with Zakaria"
love_count = msg.lower().count('love')
t_count = msg.lower().count('t')
print(f"Number of 'Love' is: {love_count}")
print(f"Number of 't' is: {t_count}")

# q19
msg = "I %7 Python And Although I %7 GSG with Zakaria"
updated_msg = msg.replace('%7', 'Love', 1)
print(updated_msg)

# q20
def is_symmetrical(s):
    cleaned_s = re.sub(r'[\s.,]', '', s.lower())
    return cleaned_s == cleaned_s[::-1]
def is_palindrome(s):
    cleaned_s = re.sub(r'[\s.,]', '', s.lower())
    return cleaned_s == cleaned_s[::-1]
tests = ["ZakZak", "Zakaria", "A war at Tarawa.", "madam"]
for test in tests:
    symmetrical = is_symmetrical(test)
    palindrome = is_palindrome(test)
    print(f"{test} is {'symmetrical' if symmetrical else 'NOT symmetrical'}, and {test} is {'a palindrome' if palindrome else 'NOT a palindrome'}.")




