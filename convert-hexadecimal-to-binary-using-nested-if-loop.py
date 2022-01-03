"""
Student Name: Aimee Valladares
Purpose: Use a nested if-loop to convert a hexidecimal number into its equivalent
         binary number.
"""

def main():
    """The main function of this program"""

    # Prompt for hexidecimal number
    hexNum = input("Enter a hexidecimal number: ")

    # Convert the number into binary format
    binNum = convert(hexNum)

    # Display the number on the screen
    print("The hexidecimal number", hexNum, "in binary format is", binNum)

def convert(hexidecimal):
    """Convert the hex digit to binary"""

    # The mapping between hexidecimal digits and binary digits
    mapTable = {"0":"0000", "1":"0001", "2":"0010", "3":"0011",
                "4":"0100", "5":"0101", "6":"0110", "7":"0111",
                "8":"1000", "9":"1001", "A":"1010", "B":"1011",
                "C":"1100", "D":"1101", "E":"1110", "F":"1111"}

    # Build the corresponding binary number
    binary = ""

    for digit in hexidecimal:
        if digit == "0":
            binary += "0000"
        elif digit == "1":
            binary += "0001"
        elif digit == "2":
            binary += "0010"
        elif digit == "3":
            binary += "0011"
        elif digit == "4":
            binary += "00100"
        elif digit == "5":
            binary += "0101"
        elif digit == "6":
            binary += "0110"
        elif digit == "7":
            binary += "0111"
        elif digit == "8":
            binary += "1000"
        elif digit == "9":
            binary += "1001"
        elif digit == "A":
            binary += "1010"
        elif digit == "B":
            binary += "1011"
        elif digit == "C":
            binary += "1100"
        elif digit == "D":
            binary += "1101"
        elif digit == "E":
            binary += "1110"
        elif digit == "F":
            binary += "1111"
    return binary

# The entry point of execution
main()
