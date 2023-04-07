def sort(the_list):
    new_list = []

    for i in range(len(the_list)):
        minimum = get_minimum_element_in_a_list(the_list)
        new_list.append(minimum)
        the_list.remove(minimum)

    return new_list


def get_minimum_element_in_a_list(the_list: list):
    minimum_element = the_list[0]

    for i in the_list:
        if i < minimum_element:
            minimum_element = i

    return minimum_element