
import random

def geramat(qntLinhas, qntColunas, min, max):


	mat = []
	for linha in range(qntLinhas):
		
		linha = []
		for coluna in range(qntColunas):
			linha.append(random.randint(min, max))
		mat.append(linha)


	return mat

def printmat(mat):

	lin = len(mat[0])
	col = len(mat)
	for linhas in range(col):
		for colunas in range(col):
			print('%5d' % mat[linhas][colunas], ' ', end='')
		print()

def trocacoluna(mat, c1, c2):


	troca = []

	for i in mat:
		troca = mat[i][c1]
		mat[i][c2] = mat[i][c1]
		mat[i][c1] = troca

	return mat


def somamat(mat1, mat2):



	lst = []
	num = 0
	soma = []

	for linha in range(len(mat1)):
		for coluna in range(len(mat2)):
			num = mat1[linha][coluna] + mat2[linha][coluna]
			lst.append(num)	
		soma.append(lst)
		lst = []
		num = 0

	return soma 

def trocalinha(mat, l1, l2):

    x = []
    for i in range(len(mat)):
        x = mat[l1]
        mat[l1] = mat[l2]
        mat[l2] = x



    return mat
