def find_uniq(arr):
    """
    Encontra o número único em uma lista de inteiros.

    Args:
        arr (list of int): Uma lista de inteiros onde se deseja encontrar o número único.

    Returns:
        int: O número único na lista.
        
    # Para mais informações ; https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python    
    """   
    # A ideia,é  se o primeiro e o segundo elementos da lista forem iguais,o "comum" (que se repete) pode ser um dos dois 
    # Se o primeiro e o segundo elementos são diferentes.
    # O terceiro (ou demais) são iguais porque a lista contém apénas um único elemento,
    # então esse "unico", está provalmente se encontra no indice (0 ou 1)
    comum = arr[0] if arr[0] == arr[1] else arr[2]
        
    for n in arr:
        if n != comum:
            return n

# Exemplos de uso
print(find_uniq([1, 1, 1, 2, 1, 1]))  # Deve retornar 2
print(find_uniq([0, 0, 0.55, 0, 0]))  # Deve retornar 0.55
print(find_uniq([3, 10, 3, 3, 3]))  # Deve retornar 10
