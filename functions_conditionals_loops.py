# Conditionals

number = 12
if number > 10:
    print ('This number is greater than 10.')
else:
    print ('This number is less than 10')

if 10 < 100:
    print ('Yup')

# Functions

def name_printer(name, value):
    print (name, value)

name_printer('Tony', 123)

# For Loops

for i in [1, 2, 3, 4, 5]:
    print ("VALUE: ", i)

for i in range(20):
    print ('VALUE: ', i)

# While Loops

x = 10

while x > 0:
    print ('x is still greater than zero')
    x = x-1
