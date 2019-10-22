# Ask a user their name
naam = input("What's your name? ")

# If their first name starts with A or B 
eerste_letter = naam[0:1]
if eerste_letter.upper() in ('A','B'):
# tell them they go to room AB
    room = 'AB'
# IF their first name starts with C
elif eerste_letter.upper() == 'C'
# tell them to go to room CD
    room = 'CD'
# If their first name starts with another letter, ask for their last name
else:
    achternaam = input("What's your last name? ")
# IF their last name starts with Z, tell them to go to room Z
    eerste_letter2 = achternaam.upper()
    if eerste_letter2 == 'Z':
    room = 'Z'
# if their last name starts with any other letter, tell them to go to room OTHER
    else:
    room = 'OTHER'
# When you are done
# Anna should be in room AB
# Bob should be in room AB
# Charlie should be in room C
# Khalid Haque should be in room OTHER
# Xin Zhao should be in room Z