def find_uniq(arr):
    """
    Encontra o número único em uma lista de inteiros.

    Args:
        arr (list of int): Uma lista de inteiros onde se deseja encontrar o número único.

    Returns:
        int: O número único na lista.
        
    # Para mais informações ; https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python    
    """   
    # Cria um dicionário para armazenar as contagens de ocorrências de cada elemento
    cont = {}
    
    # Itera sobre o array
    for n in arr: 
        # Se a chave já existe no dicionário, incrementa o contador de ocorrências
        if n in cont:
            cont[n] += 1
        else:
            # Se a chave não existe no dicionário, cria a chave com contagem igual a 1
            cont[n] = 1
    
    # Itera pelo dicionário de contagens
    for chave, valor in cont.items():
        # Retorna a chave (elemento) com valor igual a 1, que é o elemento único
        if valor == 1:
            return chave

# Exemplos de uso
print(find_uniq([1, 1, 1, 2, 1, 1]))  # Deve retornar 2
print(find_uniq([0, 0, 0.55, 0, 0]))  # Deve retornar 0.55
print(find_uniq([3, 10, 3, 3, 3]))  # Deve retornar 10
