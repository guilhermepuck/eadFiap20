equipamentos = []
valores = []
numeroSerial = []
departamento = []
responda = "S"

# Atribuindo informação nas listas e fazendo um laço de repetição
while responda == "S":
    equipamentos.append(input('Equipamento: '))
    valores.append(float(input('Valor: ')))
    numeroSerial.append(int(input('Número Serial: ')))
    departamento.append(input('Departamento: '))
    responda = input('Digite \"S\" para continuar: ').upper()

# Verificando as listas e mostrando os resultados
for indice in range(0, len(equipamentos)):
    print('\nEquipamento:....: ', (indice + 1))
    print('Nome............: ', equipamentos[indice])
    print('Valor...........: ', valores[indice])
    print('Serial..........: ', numeroSerial[indice])
    print('Departamento....: ', departamento[indice])

# Busca dentro da lista
busca = input('\nDigite o nome do equipamento que deseja buscar: ')
for indice in range(0, len(equipamentos)):
    if busca == equipamentos[indice]:
        print('Valor..:', valores[indice])
        print('Serial.:', numeroSerial[indice])

# Gera uma depreciação no valor do equipamento
depreciacao = input('Digite o nome do equipamento que será depreciado: ')
for indice in range(0, len(equipamentos)):
    if depreciacao == equipamentos[indice]:
        print('Valor antigo: ', valores[indice])
        valores[indice] = valores[indice] * 0.9
        print('Novo valor: ', valores[indice])

# Deletando um item da lista
Serial = int(input('Digite o serial do equipamento que será excluido: '))
for indice in range(0, len(departamento)):
    if numeroSerial[indice] == Serial:
        del departamento[indice]
        del equipamentos[indice]
        del numeroSerial[indice]
        del valores[indice]
        break
