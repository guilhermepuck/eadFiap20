inverntario = []
resposta = "S"
while resposta == "S":
    inverntario.append(input('Equipamento: '))
    inverntario.append(float(input('Valor: ')))
    inverntario.append(int(input('Número Serial: ')))
    inverntario.append(int(input('Departamento: ')))
    resposta = input('Digite \"S\" para continuar: ').upper()

for elemento in inverntario:
    print(elemento)
