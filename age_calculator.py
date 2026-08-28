b_year = input("Enter Your Birth Year:")

if not b_year.isdigit(): # it will give error if birth year is not integer 
    print("Invalid")
    exit()

b_year = int(b_year) #it convert the string to integer because b.year is save as string
if b_year <1946:
    print("The Life Expectancy at Birth is Approx 80")
    exit()

import datetime
c_year = datetime.datetime.now().year #it gets current year

if b_year >= c_year:
    print(" Wait For Your Birth")
    exit()

age = (c_year - b_year)
print("Your age is",age)

