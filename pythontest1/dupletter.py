def duplicate_letters(input_string):
    """
    This function takes a string as input and returns a new string with all duplicate letters removed.

    Parameters:
    input_string (str): The string from which duplicate letters will be removed.

    Returns:
    str: A new string with duplicate letters removed.
    """
    seen = set()
    result = []

    for char in input_string:
        if char not in seen:
            seen.add(char)
            result.append(char)

    return "".join(result)


text = "Pythyon"
print(duplicate_letters(text))
