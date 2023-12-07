import random

# Welcome message
print('This is a Password Generator\n')

# Charac for Passwords
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_.,1234567890'

# Get user input for the number of passwords and password length
number = int(input('Amount of passwords to generate: '))
length = int(input('Input your password length: '))

# Display a header for the generated passwords
print('\nHere are your passwords:')

# Generate Passwords
for pwd in range(number):
    # Store the password
    password = ''

    # Generate the password with the specified length
    for c in range(length):
        password += random.choice(chars)

    # Print Password
    print(password)

