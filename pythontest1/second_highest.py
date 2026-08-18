def second_highest(numbers):
    highest = numbers[0]
    second = numbers[0]

    for n in numbers:
        if n > highest:
            second = highest
            highest = n
        elif n > second and n != highest:  # [8,3,6,3] i.e 6>3 and 6!=8 !!!
            second = n

    return second
