def is_palindrome(input_string):
    # Convert the input string to lowercase and remove non-alphanumeric characters
    cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())

    # Check if the cleaned string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]

user_input = input("Enter a string: ")
if is_palindrome(user_input):
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")
