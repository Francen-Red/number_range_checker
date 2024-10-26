# Create an empty list to store inputted numbers
inputted_numbers = []

# Create a list that only accepts numbers 1-50 and adds the current valid number to it
acceptable_numbers = list(range(1, 51))

# Initialize counters for each range
first_range = 0
second_range = 0
third_range = 0
fourth_range = 0
fifth_range = 0

# Create a while loop for the inputted number to check its validity
while True:
        # Ask user to input a number and convert it to integer
        input_number = int(input("Please input a number between 1 and 50: "))
        # Check the validity of the number
        # If the inputted number is within the range of acceptable_numbers, append the number to the empty list and continue
        if input_number in acceptable_numbers:
            inputted_numbers.append(input_number)
            continue
        # Else, print an error message and break the loop
        else:
            print("Invalid input! Please enter a number ranging from 1-50")
        break

# Create a for loop to iterate over each number in the list
for input_number in inputted_numbers:
    # Use if-statements to check which range the current number falls into
    if 1 <= input_number <= 10:
        first_range += 1            # Increment to corresponding range counter
    elif 11 <= input_number <= 20:
        second_range += 1           # Increment to corresponding range counter
    elif 21 <= input_number <= 30:
        third_range += 1            # Increment to corresponding range counter
    elif 31 <= input_number <= 40:
        fourth_range += 1           # Increment to corresponding range counter
    elif 41 <= input_number <= 50:
        fifth_range += 1            # Increment to corresponding range counter

# Display the number of input for each range
print("\nNumber of valid input in each range:")
print("Range of 1-10:", first_range)
print("Range of 11-20:", second_range)
print("Range of 21-30:", third_range)
print("Range of 31-40:", fourth_range)
print("Range of 41-50:", fifth_range)




       



       
