nome=input('Digite o nome:')
idade=int(input('Digite a sua idade:'))
doenca_infectocontagiosa=input('Suspeita de doença infecto-contagiosa?').upper()
if idade > 65 and doenca_infectocontagiosa == 'SIM':
    print('O paciente será direcionado para a sala AMARELA - COM prioridade')
elif idade < 65 and doenca_infectocontagiosa == 'SIM':
    print('O paciente será direcionado para sala AMARELA - SEM prioridade')
elif idade >= 65 and doenca_infectocontagiosa == 'NÃO':
    print('O paciente será direcionado para sala BRANCA - COM prioridade')
elif idade < 65 and doenca_infectocontagiosa == 'NÃO':
    print('O paciente será direcionado para sala BRANCO - SEM prioridade')
else:
    print('Responda a suspeita de doença infectocontagiosa com SIM ou NÃO')
