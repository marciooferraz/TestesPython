#Arrays em Python

arrayFamily = ['Márcio', 'Cintia', 'Janaina']

arrayFamily.append('Xablau') #Método append() acrescenta valor a lista. Valor será sempre incuido na ultima posição da lista
print('Qual o menbro mais novo da familia? %s'%arrayFamily[2])

print('\nO mais bonitão: %s'%arrayFamily[-1])

print('\nEscrea todos os nomes da lista:')

#contador = 0
for contador in range(4) : 
    print(arrayFamily[contador])

arrayFamily.remove(arrayFamily[-1]) #Método remove() exclui um item da lista, pode se usar a posição ou mesmo o nome do item
contador = 0
print('\nEscreva novamente todos os nomes da porra da lista: ')
for contador in range(3) :
    print(arrayFamily[contador])

del arrayFamily[0] #comando del exclui um item da lista somente através da posição
contador = 0
print('\nEscreva novamente todos os nomes da porra da lista: ')
for contador in range(2) :
    print(arrayFamily[contador])

print(arrayFamily.index('Janaina')) #Método index pesquisa um valor na lista e retorna a posição

tamanhoArray = len(arrayFamily) #Método len() retorna o tamanho do array
print(tamanhoArray)

print('')

for teste in arrayFamily :
    print(teste)

arrayFamily.append('Márcio')
arrayFamily.append('Ana')

arrayFamily.sort()  #Método sort() Ordena a lista em ordem alfabética

print('\n\nMenbros da Familia em ordem alfabética')
for membroFamilia in arrayFamily :
    print(membroFamilia)
