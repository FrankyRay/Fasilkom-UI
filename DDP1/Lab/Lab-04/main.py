# Name   : Franky Raymarcell Sinaga
# NPM    : 23xxxxxxxx
# TA Code: XXX

# Return numbered line
def lineNumber(line, text):
    return f"{line:03d}. {text}"

# Main program
def main():
    # Ask the user the input and output file
    file_input = input("Input file name: ")
    file_output = input("Output file name: ")

    try:
        # Try open the file
        with open(file_input) as file:
            data = file.readlines()

        # Add line number to all lines using lineNumber function
        numLines = "".join([lineNumber(i, ln) for i, ln in enumerate(data)])
        # Count the letters
        letters = len([chr for chr in "".join(data) if chr.isalpha()])

        # Write the output to the output file
        with open(file_output, "w") as file:
            file.write(f"{numLines}\n\nThe total number of letters in the file {file_input} is {letters}")
    
    # Print error message when input file is not found
    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    # Run the program when script is running
    try:
        main()

    # Skip the program when user use CTRL + C
    except KeyboardInterrupt:
        pass