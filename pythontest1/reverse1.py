def reverse_string(s):
    """
    Reverses the input string.

    Args:
        s (str): The string to be reversed.

    Returns:
        str: The reversed string.
    """
    # return s[::-1]

    #  ********* 2 *************

    result = ""
    i = len(s) - 1
    while i >= 0:
        result += s[i]
        i -= 1
    return result


text = "Python"
print(reverse_string(text))
