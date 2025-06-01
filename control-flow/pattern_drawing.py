# Prompt user for the size of the pattern (positive integer)
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter for the while loop
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Use a for loop to print 'size' asterisks in the current row
    for _ in range(size):
        print("*", end="")
    # After printing the row, print a newline to move to the next row
    print()
    # Increment the row counter
    row += 1
