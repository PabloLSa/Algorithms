def is_palindrome_recursive(word, low_index, high_index):
    """
    Verifica se a palavra é um palíndromo de forma recursiva.

    """
    # Caso base: se a palavra for vazia, não é um palíndromo
    if len(word) == 0:
        return False

    # Caso base: se o índice inicial for maior ou igual ao índice final, a palavra é um palíndromo
    if low_index >= high_index:
        return True

    # Verifica se os caracteres nos índices baixo e alto são iguais
    first = word[low_index]
    last = word[high_index]
    if first == last:
        # Recursivamente, verifica o restante da palavra, movendo os índices para dentro
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    else:
        return False

