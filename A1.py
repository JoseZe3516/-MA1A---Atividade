#1
def valor (produto):
    nProduto = produto
    produto = ['Salgado', 'Refrigerante', 'Suco', 'Sorvete', 'Cafe', 'Capuccino', 'Bolo', 'Dadinho']
    preco = [4.0, 4.5, 5.0, 6.0, 4.0, 6.0, 4.5, 0.5]
    for n in range(len(produto)):
        if produto[n] == nProduto:
            return preco[n]
print(valor('Salgado'))




#2
def pessoas():
    
    nomes = []
    pedidos = []
    for n in range(7):
        iNomes = input('Nome do aluno: ')
        iPedidos = input('Pedido feito pelo aluno: ')
        nomes.append(iNomes)
        pedidos.append(iPedidos)
    return [nomes, pedidos] 




#3
def pagamento ():
    produto = ['Salgado', 'Refrigerante', 'Suco', 'Sorvete', 'Cafe', 'Capuccino', 'Bolo', 'Dadinho']
    preco = [4.0, 4.5, 5.0, 6.0, 4.0, 6.0, 4.5, 0.5]
    pessoas1 = pessoas()[0]
    fila = pessoas()[1]
    soma = 0
    for n in range(7):
        valor1 = valor(fila[n])
        soma += valor1
        print(pessoas1[n], fila[n], valor1)
    print('Valor final {}'.format(soma))
pagamento()
    





