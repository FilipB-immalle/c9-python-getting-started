# Ask a user to enter a number
number = input('Please enter a number. ')

# Ask a user to enter a second number
number2 = input('Please enter a second number. ')

# Calculate the total of the two numbers added together
answer = int(number) + int(number2)

# Print 'first number + second number = answer' 
# For example if someone enters 4 and 6 the output should read
# 4 + 6 = 10
print(number + ' + ' + number2 + " = " + str(answer))