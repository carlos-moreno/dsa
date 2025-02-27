package main

import "fmt"

// append adiciona um valor ao final de um slice de inteiros, criando um novo slice.
// Ele copia os elementos do slice original para um novo slice com espaço adicional para o novo valor.
// Parâmetros:
//   - array: Slice de inteiros original.
//   - value: Valor inteiro a ser adicionado ao final do slice.
//
// Retorno:
//   - Um novo slice de inteiros contendo todos os elementos do original e o novo valor.
func append(array []int, value int) []int {
	var length = len(array)
	var tempArray = make([]int, length+1)

	for i := range array {
		tempArray[i] = array[i]
	}
	tempArray[length] = value
	return tempArray
}

// OneArrayAppend demonstra o uso da função append para adicionar um elemento a um slice.
// Ele inicializa um slice de inteiros, adiciona um novo valor e imprime os valores resultantes.
func OneArrayAppend() {
	var scores = []int{90, 70, 50, 80, 60, 85}
	scores = append(scores, 75)

	for _, score := range scores {
		fmt.Printf("%d ", score)
	}
	fmt.Println()
}
