#!/usr/bin/env python3
"""Algoritmo de Pesquisa Binária"""


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


if __name__ == "__main__":
    print(pesquisa_binaria([1, 2, 3, 4, 5], 3))
    print(pesquisa_binaria([1, 2, 3, 4, 5], 6))
    print(pesquisa_binaria([1, 2, 3, 4, 5], 2))
    print(
        pesquisa_binaria(
            [
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                10,
                11,
                12,
                13,
                14,
                15,
                16,
                17,
                18,
                19,
                20,
            ],
            19,
        )
    )
