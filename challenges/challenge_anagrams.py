def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if not first_string or not second_string:
        return False
    first_list = convert_to_ascii_code_array(first_string)
    second_list = convert_to_ascii_code_array(second_string)
    order_quick(first_list, 0, len(first_list)-1)
    order_quick(second_list, 0, len(second_list)-1)
    pos = 0
    equals = True
    while pos < len(first_list) and equals:
        if first_list[pos] == second_list[pos]:
            pos += 1
        else:
            equals = False
    return equals


def convert_to_ascii_code_array(string):
    string_list = list(string.lower())
    new_list = []
    for char in string_list:
        new_list.append(ord(char))
    return new_list


def order_quick(array, start, end):
    if len(array) == 1:
        return array
    if start < end:
        p = partition(array, start, end)
        order_quick(array, start, p - 1)
        order_quick(array, p + 1, end)


def partition(array, start, end):
    pivot = array[end]
    delimiter = start - 1

    for index in range(start, end):
        if array[index] <= pivot:
            delimiter = delimiter + 1
            array[index], array[delimiter] = array[delimiter], array[index]

    array[delimiter + 1], array[end] = array[end], array[delimiter + 1]

    return delimiter + 1


# REF: https://panda.ime.usp.br/panda/static/pythonds_pt/02-AnaliseDeAlgori
# tmos/ExemploDeDeteccaoDeAnagramas.html#:~:text=Um%20bom%20exemplo%20de%20
# problema,e%20'roma'%20s%C3%A3o%20anagramas.
