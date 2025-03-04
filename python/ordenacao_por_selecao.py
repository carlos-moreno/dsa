#!/usr/bin/env python3
"""Algoritmo de Ordenação por Seleção

No caso abaixo, será apresentado um ordenação de
array do menor para o maior elemento."""


def buscar_menor(arr):
    """Busca o menor elemento do array.

    Args
    ----
        arr: list
            O array onde o menor elemento será buscado.

    Returns
    -------
        int:
            O índice do menor elemento no array.
    """

    menor = arr[0]
    menor_indice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice


def ordenacao_por_selecao(arr):
    """Realiza uma ordenação por seleção do menor elemento para o maior.

    Args
    ----
        arr: list
            O array a ser ordenado.

    Returns
    -------
        list:
            O array ordenado do menor elemento para o maior.

    Exemplos:
        >>> ordenacao_por_selecao([5, 3, 6, 2, 10])
        [2, 3, 5, 6, 10]
        >>> ordenacao_por_selecao([5, 3, 6, 2, 10, 0, 100, 72, 71])
        [0, 2, 3, 5, 6, 10, 71, 72, 100]
    """

    novo_arr = []
    for i in range(len(arr)):
        menor = buscar_menor(arr)
        novo_arr.append(arr.pop(menor))
    return novo_arr


if __name__ == "__main__":
    print(ordenacao_por_selecao([]))
    print(ordenacao_por_selecao([1]))
    print(ordenacao_por_selecao([5, 3, 6, 2, 10]))
    print(ordenacao_por_selecao([5, 3, 6, 2, 10, 0, 100, 72, 71]))
    print(ordenacao_por_selecao([5, 3, 6, 2, 10, 0, 100, 72, 71, 71, 71, 70]))
