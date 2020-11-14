equipamento = []
valor = []
serial = []
departamento = []
responda = "S"

'''while responda == "S":
    equipamento.append(input('Equipamento: '))
    valor.append(float(input('Valor: ')))
    serial.append(int(input('Número Serial: ')))
    departamento.append(int(input('Departamento: ')))
    responda = input('Digite \"S\" para continuar: ').upper()

# Eliminando um item da lista
serial = int(input('Digite o serial do equipamento que será excluido: '))
for indice in range(0, len(departamento)):
    if seriais[indice] == serial:
        del departamento[indice]
        del equipamento[indice]
        del seriais[indice]
        del valor[indice]
        break
# Verificando as listas e mostrando os resultados
for indice in range(0, len(equipamento)):
    print('\nEquipamento:....: ', (indice + 1))
    print('Nome............: ', equipamento[indice])
    print('Valor...........: ', valor[indice])
    print('Serial..........: ', seriais[indice])
    print('Departamento....: ', departamento[indice])'''

seriais=int(input("\nDigite o serial do equipamento que será excluido: "))
for indice in range(0, len(departamento)):
    if seriais[indice]==serial:
        del departamento[indice]
        del equipamento[indice]
        del serial[indice]
        del valor[indice]
        break

for indice in range(0,len(equipamento)):
    print("\nEquipamento..: ", (indice+1))
    print("Nome.........: ", equipamento[indice])
    print("Valor........: ", valor[indice])
    print("Serial.......: ", serial[indice])
    print("Departamento.: ", departamento[indice])