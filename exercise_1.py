# Exercise 1 
# Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.

def max_of_three(x,y,z):
    # Store argumens in dict
    nums = {'x': x, 'y': y, 'z': z}
    # Use max method to find highest value inside dict
    highest = max(nums.values())
    
    # Iterate through the dict
    for key, value in nums.items():
        # filter highest value and print to screen
        if value == highest:
            print(value)


max_of_three(20, 1, 11)