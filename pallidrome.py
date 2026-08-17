def pallidrome(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()

    # Check if the string is equal to its reverse
    if s == s[::-1]:
        return "This is a palindrome"
    else:
        return "This is not a palindrome"


text = "element"
print(pallidrome(text))
