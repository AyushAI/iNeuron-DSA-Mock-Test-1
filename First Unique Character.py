def firstUniqChar(s):
    """
    Finds the index of the first non-repeating character in a string.
    """
    char_freq = {}  # Dictionary to store the frequency count of characters

    # Count the frequency of each character in the string
    for char in s:
        char_freq[char] = char_freq.get(char, 0) + 1

    # Find the index of the first non-repeating character
    for i in range(len(s)):
        if char_freq[s[i]] == 1:
            return i

    return -1  # Return -1 if no non-repeating character is found

# Example usage:
s = "leetcode"
print(firstUniqChar(s))
