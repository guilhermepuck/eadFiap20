nivel = input('Digite o nivel de acesso: ').upper()
if nivel == 'ADM' or nivel == 'USR':
    genero = input('Digite o seu gênero: ').upper()
    if nivel == 'ADM':
        if genero == 'FEMININO':
            print('Olá administradora')
        else:
            print('Olá administrador')
    else:
        if genero == 'FEMININO':
            print('Olá usuário')
        else:
            print('Olá usuária')
elif nivel == 'GUEST':
    print('Olá visitante')
else:
    print('Olá desconhecido(a)')
