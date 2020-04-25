import csv

# Trabalhando com arquivos em Python

#Modos de acesso > accessMode
# w => Gravação
# a => inclui no final
# r => Leitura
# b => Abrir


fileName = 'UmArquivo.txt'
WRITE = 'w'
APPEND = 'a'
READ = 'r'
OPEN = 'b'

#file = open(fileName, APPEND)
#file.write('Xablau, xablau xablau!!!\n')
#file.write('Mais uma linha de xablau!!!\n')
#file.close()

#print('A porra do arquivo foi gravado com exito!!!')

#file = open(fileName, '')

with open("UmOutroArquivo.txt", "r") as outroFile :
    linhas = csv.reader(outroFile)

    for linhaAtual in linhas :
        print(linhaAtual)

#conteudoOutroFile = outroFile.read()
#sasuke = outroFile.readline()
#ichigo = outroFile.readline()

#print()
##print(conteudoOutroFile)
#print('Sasuke: %s'%sasuke)
#print('Ichigo: %s'%ichigo)

