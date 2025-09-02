
def taking_input():
    global nums, target
    nums = []
    xmas = int(input("How many integers would you like to add in the array: "))
    for i in range(xmas):
        ullu = int(input(f"Please enter the {i+1}th integer value: "))
        nums.append(ullu)
    target = int(input("Please enter the integer that should be the sum target: "))
    
    print(f"\nThe array prepared from your inputs is: {nums}")
    print(f"The target sum is: {target}")

def two_sum():
    # Dictionary to store value -> index
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            print(f"\nIndices of numbers that add up to {target}: {num_map[complement]}, {i}")
            return
        num_map[num] = i
    print("\nNo two numbers add up to the target.")

# Run the functions
taking_input()
two_sum()
