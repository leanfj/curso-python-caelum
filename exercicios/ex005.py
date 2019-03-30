lista = list()

continuar = True

while continuar:
    pessoa = dict()
    pessoa['nome'] = input('Informe o nome: ')
    pessoa['idade'] = input('Informe a idade: ')
    pessoa['cidade'] = input('Informe a Cidade: ')

    lista.append(pessoa)

    opcao = input('Digite S para continuar a incluir e N para terminar\n')
    if(opcao.upper() == 'N'):
        continuar = False

for item in lista:
    print('Nome: {}'.format(item['nome']))
    print('Idade: {}'.format(item['idade']))
    print('Cidade: {}'.format(item['cidade']))
    print('\n')
