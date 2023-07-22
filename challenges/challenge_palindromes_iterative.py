def is_palindrome_iterative(word):
    """
    Verifica se uma palavra é um palíndromo de forma iterativa.

    Args:
        word (str): A palavra a ser verificada.

    Returns:
        bool: True se a palavra for um palíndromo, False caso contrário.
    """
    # Verificar se a palavra é uma string vazia
    if not word:
        return False

    # Remover espaços e tornar todas as letras minúsculas
    cleaned_word = "".join(char.lower() for char in word if char.isalpha())

    # Verificar se a palavra é um palíndromo
    for i in range(len(cleaned_word) // 2):
        if cleaned_word[i] != cleaned_word[-(i + 1)]:
            return False

    return True
