def moveZeroes(nums):
    """
    Moves all zeroes to the end of the array while maintaining the order of non-zero elements.
    """
    zero_ptr = 0  # Pointer to keep track of the position to place the next non-zero element

    # Traverse the array and swap non-zero elements with the position pointed by zero_ptr
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero_ptr] = nums[zero_ptr], nums[i]
            zero_ptr += 1

# Example usage:
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)
