def find_duplicate(nums):
    """
    
        nums (list): Uma lista de números inteiros positivos.

    Returns:
      
    """
    # Verificar se a entrada é válida
    if not all(isinstance(num, int) and num > 0 for num in nums):
        return False

    num_set = set()

    for num in nums:
        if num in num_set:
            return num

        num_set.add(num)

    return False
