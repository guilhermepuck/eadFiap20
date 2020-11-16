from Funcao.IdentificacaoDeFuncoes import *

minhaLista=[]
print("Preenchendo")
preencherInventario(minhaLista)
print("Exibindo")
exibirInventerio(minhaLista)

print("Pesquisando")
localizaPorNome(minhaLista)
print("Alterando")
depreciarPorNome(minhaLista, 20)

print("Excluindo")
print(excluirPorSerial(minhaLista))
exibirInventerio(minhaLista)

print("Resumindo")
resumirValores(minhaLista)