def is_anagram(first_string, second_string):
    # Obter as strings ordenadas
    sorted_first_string = get_sorted_string(first_string)
    sorted_second_string = get_sorted_string(second_string)

    # Verificar se alguma das palavras é uma string vazia
    if sorted_first_string == "" or sorted_second_string == "":
        return (sorted_first_string, sorted_second_string, False)
    else:
        # Comparar as strings ordenadas para determinar se são anagramas
        are_anagrams = sorted_first_string == sorted_second_string
        return (sorted_first_string, sorted_second_string, are_anagrams)


def get_sorted_string(string):
    # Converter a string em uma lista de caracteres em minúsculo
    char_list = list(string.lower())

    # Ordenar a lista de caracteres utilizando o Merge sort
    merge_sort(char_list)

    # Juntar os caracteres ordenados em uma única string
    sorted_string = "".join(char_list)
    return sorted_string


def merge_sort(chars):
    # Implementação do Merge sort para ordenar a lista de caracteres
    if len(chars) > 1:
        middle = len(chars) // 2
        left_half = chars[:middle]
        right_half = chars[middle:]

        merge_sort(left_half)
        merge_sort(right_half)

        merge(chars, left_half, right_half)


def merge(chars, left, right):
    # Função auxiliar para mesclar duas metades ordenadas
    left_index, right_index, merged_index = 0, 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            chars[merged_index] = left[left_index]
            left_index += 1
        else:
            chars[merged_index] = right[right_index]
            right_index += 1
        merged_index += 1

    while left_index < len(left):
        chars[merged_index] = left[left_index]
        left_index += 1
        merged_index += 1

    while right_index < len(right):
        chars[merged_index] = right[right_index]
        right_index += 1
        merged_index += 1
