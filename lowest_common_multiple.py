def get_lcm(number):
    the_list = []
    if number == 1:
        the_list.append(1)
        return the_list

    if number == 2:
        divider = 2
        while divider <= number:
            the_list.append(divider)
            divider -= 1
            the_list.append(divider)
            break
        return the_list

    divisor = 1
    while divisor <= number:
        if number % divisor == 0:
            number = number / divisor
            the_list.append(divisor)
            divisor = 1

        else:
            divisor += 1
    return the_list
