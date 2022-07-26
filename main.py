# um arquivo pode ser aberto em modo de leitura ou de edição
# w para editar (write)
# r para ler (read)

with open ('meuarquivo.txt ', 'w') as arquivo:
    arquivo.write('Ola, mundo')


# nessa segunda opção é necessário criar uma linha de código para fechar o arquivo
# enquanto na estrutura acima, utilizando o with, o código é encerrado e o arquivo encerrado assim que sair da indentação
#arquivo = open('meuarquivo.txt ', 'w')
#arquivo.write('Ola, mundo!')
#arquivo.close()
