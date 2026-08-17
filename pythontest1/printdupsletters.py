def duplicate_letters(input_string):
    seen = set()
    duplicates = set()

    for char in input_string:
        if char in seen:
            duplicates.add(char)
        else:
            seen.add(char)

    return seen, duplicates


word = "programming"

seen, duplicates = duplicate_letters(word)

print("Seen:", seen)
print("Duplicates:", duplicates)
