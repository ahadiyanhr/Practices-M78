
# Get a string from user (Akbar)
new_string = input("Enter a string:> ")

# STEP 1:
# Remove all whitespace in string using 'replace method'
del_space = new_string.replace(" ", "")

# STEP 2:
# Replace all vowels with a dot using 'replace method'
del_vowel = del_space
for vowel in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
    del_vowel = del_vowel.replace(vowel , ".")
    
# STEP 3:
# Solution 1/3: Convert all upper case to lower case and vice versa using 'swapcase method'
swap_case = del_vowel.swapcase()

# Solution 2/3: Convert all upper case to lower case and vice versa without 'swapcase method'
i = 0
swap_letter = del_vowel # Assign modified string from STEP 2 to a new string (swap_letter) for using in a loop

for letter in del_vowel:
    if letter.islower():    # Checking the letter is lower case or not
        swap_letter = swap_letter[:i] + letter.upper() + swap_letter[i+1:]  # Replace upper case using string slicing
    elif letter.isupper():    # Checking the letter is upper case or not
        swap_letter = swap_letter[:i] + letter.lower() + swap_letter[i+1:]  # Replace lower case using string slicing
    i += 1


''' Print final result '''
print(swap_case)    # Result from Solution 1/3
print(swap_letter)    # Result from Solution 2/3