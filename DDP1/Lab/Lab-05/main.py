def make_new_row(old_row: list[int]):
    """Create next pascal row from previous row"""
    result = [1]
    for i in range(len(old_row)):
        if i == len(old_row) - 1: result += [1]
        else: result += [old_row[i] + old_row[i + 1]]
    return result

def main():
    # Get user's input and validate it
    height: str = input("Enter the height of Pascal's triangle (integer > 2): ")
    while not height.isdigit() or int(height) <= 2:
        print("Invalid input")
        height: str = input("Enter the height of Pascal's triangle (integer > 2): ")

    # Print the list
    print("\nPrinting the whole list of lists:")
    print("[")

    # Save the pascal sequence into list and initiate data
    pascal_str = []
    data = []

    # Create pascal sequence based of user input: height
    for _ in range(int(height)):
        # Get the new pascal row
        data = make_new_row(data)
        # Append the string version of pascal row
        pascal_str.append(" ".join([str(n) for n in data]))
        # Print the list version of pascal row
        print("  " + str(data))
    print("]")

    # Take the longest length of string and use it for centering the pascal seq
    longest_chr = len(pascal_str[-1])
    print(f"Pascal's triangle of height {height}: ")
    print("\n".join([pascal.center(longest_chr) for pascal in pascal_str]))

    # Ask user to press "Enter" for terminate the program
    input("\nPress Enter to exit ...")

if __name__ == '__main__':
    main()