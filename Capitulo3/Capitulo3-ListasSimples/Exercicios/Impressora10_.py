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
    departamento.append(int(input('Departamento: ')))
    responda = input('Digite \"S\" para continuar: ').upper()

# Verificando as listas e mostrando os resultados
'''for indice in range(0, len(equipamentos)):
    print('\nEquipamento:....: ', (indice + 1))
    print('Nome............: ', equipamentos[indice])
    print('Valor...........: ', valores[indice])
    print('Serial..........: ', numeroSerial[indice])
    print('Departamento....: ', departamento[indice])'''

# Busca dentro da lista
'''busca = input('\nDigite o nome do equipamento que deseja buscar: ')
for indice in range(0, len(equipamentos)):
    if busca == equipamentos[indice]:
        print('Valor..:', valores[indice])
        print('Serial.:', numeroSerial[indice])'''

# Depreciamento
depreciacao=input("\nDigite o nome do equipamento que será depreciado: ")
for indice in range(0,len(equipamentos)):
    if depreciacao==equipamentos[indice]:
        print("Valor antigo: ", valores[indice])
        valores[indice] = valores[indice] * 0.9
        print("Novo valor: ", valores[indice])
