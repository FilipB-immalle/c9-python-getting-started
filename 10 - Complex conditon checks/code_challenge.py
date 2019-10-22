# When you join a hockey team you get your name on the back of the jersey
# but the jersey may not be big enough to hold all the letters
# Ask the user for their first name
naam = input('Wat is je eerste naam?: ')

# Ask the user for their last name
achternaam = input('Wat is je achternaam?: ')

# if first name is < 10 characters and last name is < 10 characters 
if(len(naam) < 10 and len(achternaam) < 10):
#       print first and last name on the jersey
    print(naam + " " + achternaam)
# if first name >= 10 characters long and last name is < 10 characters
if(len(naam) >= 10 and len(achternaam) < 10):
#       print first initial of first name and the entire last name
    print(naam[0:1].capitalize() + ". " + achternaam)
# if first name < 10 characters long and last name is >= 10 characters
if(len(naam) < 10 and len(achternaam) >= 10):
#       print entire first name and first initial of last name
    print(naam +  " " + achternaam[0:1].capitalize() + ".")
# if first name >= 10 characters long and last name is >= 10 characters
if(len(naam) >= 10 and len(achternaam) >= 10):
#       print last name only
    print(achternaam)

# Test with the following values
# first name: Susan  last name: Ibach
# output: Susan Ibach
# first name: Susan  last name: ReallyLongLastName
# output: Susan R.
# first name: ReallyLongFirstName  last name: Ibach
# output: R. Ibach
# first name: ReallyLongFirstName  last name: ReallyLongLastName
# output: ReallyLongLastName