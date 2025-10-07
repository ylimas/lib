def removeNone(dic):


	remover = []

	for i in dic:
		if dic[i] == None:
			remover.append(i)

	for chave in remover:
		dic.pop(chave)

	return dic

def filtro(dic):


	filtro = int(input("Os valores devem ser maiores que: "))
	remover = []


	for chave in dic:
		if dic[chave] < filtro:
			remover.append(chave)
	for chave in remover:
		dic.pop(chave)

	return dic

def aninhar(lst1, lst2, lst3):


	lst = [] 
	dictemp = {}

	for i in range(len(lst1)):
		dictemp[lst2[i]] = lst3[i]

		lst.append(dictemp.copy())
		dictemp.clear()

	return lst
