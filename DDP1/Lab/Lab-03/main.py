# Nama    : Franky Raymarcell Sinaga
# NPM     : 23xxxxxxxx
# TA Code : XXX
# Convert decimal number into hexadecimal, and vice versa

## Decimal to Hexadecimal
print('Lab 03\n')
print('From decimal to hexadecimal')
print('---------------------------')

# Read the user's input
myInt = int(input("Give a positive integer in decimal representation: "))

# Convert the decimal into hexadecimal
hexstr = ""
# Create temp variable used for division and modulo operation
temp = myInt
while temp != 0:
    # Get the modulo of the number
    hexdigit = temp % 16
    # Convert the modulo to string and set them at the beginning of the string
    if hexdigit < 10:
        hexstr = str(hexdigit) + hexstr
    else:
        hexstr = chr(hexdigit + 55) + hexstr

    # Floor division the number
    temp //= 16

# Print the output messagew
print("The hexadecimal representation of", myInt, "is 0x" + hexstr)

## Hexadecimal to Decimal
print()
print('From hexadecimal to decimal')
print('---------------------------')

# Read the user's input
hexstr = input("Give a positive integer in hexadecimal representation: ")

# Convert the hexadecimal into decimal
newInt = 0
# Remove the suffix "0x" and reversed the string
temp = hexstr[:1:-1]
# Initiate the "power" var used for hex index
power = 0

while power != len(temp):
    # Take the char out based on the power/index
    hexdigitstr = temp[power]

    # Turn the hex number into corresponding decimal number
    # And multiply by 16 ^ (power)
    if hexdigitstr.isdigit():
        newInt += int(hexdigitstr) * (16 ** power)
    else:
        newInt += (ord(hexdigitstr.upper()) % 55) * (16 ** power)

    # Increasing the power/index value
    power += 1

# Print the output message
print('The decimal representation of', hexstr, 'is', newInt)

# End the program
print()
print('Thanks for using this program.')
print()
input('Press Enter to continue ...')