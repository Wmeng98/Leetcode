# A pangram is a sentence containing every letter in the English Alphabet
# Lowercase and Uppercase are considered the same

# Solution 1

# Create mark array and mark letters from the string
# If any letters in array are unmarked at the end, then not a panagram
# Time O(n) Space O(1)

def check_pangram(s):
    # list of 26 char and set all to false
    mark = [False] * 26

    # Convert to lowercase and iterate over
    for char in s.lower():
        # only mark is char is letter in alphabet
        if char >= 'a' and char <= 'z':
            mark[ord(char) - ord('a')] = True
    
    # Check if any letters unmarked
    for m in mark:
        if not m:
            return False
    return True


print(check_pangram('The quick brown fox jumps over the lazy dog'))
print(check_pangram('The quick brown fox jumps over the dog'))