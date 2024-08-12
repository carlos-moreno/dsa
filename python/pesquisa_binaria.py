#!/usr/bin/env python3
"""Algoritmo de Pesquisa Binária"""

__version__ = "0.1.0"
__author__ = "Carlos Moreno"
__license__ = "GPL-3.0-or-later"


def pesquisa_binaria(lista, item):
    """Realiza uma pesquisa binária em uma lista ordenada para encontrar a
    posição de um item.

    Args
    ----
        lista: list
            A lista ordenada na qual a pesquisa será realizada.
        item: int
            O item que está sendo procurado na lista.

    Returns
    -------
        int:
            O índice do item na lista, se encontrado. Caso contrário, retorna
            None.

    Exemplos:
        >>> pesquisa_binaria([1, 2, 3, 4, 5], 3)
        2
        >>> pesquisa_binaria([1, 2, 3, 4, 5], 6)
        None
    """

    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]

        if chute == item:
            return meio

        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None
