# This script checks if a given string is a palindrome.
def IsPalindrome(s):
    """
    Check if the given string is a palindrome.

    :param s: Input string
    :return: True if the string is a palindrome, False otherwise
    """
    s = s.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    return s == s[::-1]

# Example usage  - True case   
if __name__ == "__main__":
    test_stringT = "Nitin"
    if IsPalindrome(test_stringT):
        print(f'"{test_stringT}" is a palindrome.')
    else:
        print(f'"{test_stringT}" is not a palindrome.')     

        # Example usage  - False case            
if __name__ == "__main__":
    test_stringF = "Pankaj"
    if IsPalindrome(test_stringF):
        print(f'"{test_stringF}" is a palindrome.')
    else:
        print(f'"{test_stringF}" is not a palindrome.')     
