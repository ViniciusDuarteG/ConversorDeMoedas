resposta = str
resultado = 0
valores = []
while resposta != "NÃO": 
    resposta = str(input("Deseja realizar alguma operação hoje?\n")).strip().upper()
    if resposta == "NÃO":
         break
    
    valor_moeda1 = str(input("Insira o valor desejado: ")).strip().replace(',','.')
    nome_moeda = str(input("Qual o nome da moeda?\n"))
    valor_moeda2 = str(input(" Para realizar essa conversão, é necessário utilizar as taxas de câmbio, que indicam a relação entre duas moedas em um determinado momento.\n\nValor em Euros = Valor em dólares x taxa de câmbio\n\n\nInsira o valor da moeda na cotação: ")).strip().replace(',','.')
    nome_moeda2 = str(input("Qual o nome da moeda?\n"))
    valor_moeda1 = float(valor_moeda1)
    valor_moeda2 = float(valor_moeda2)
    valor_moeda3 = valor_moeda1 * valor_moeda2

    print("O valor convertido de {0:.2f} {1} é equivalente a {2:.2f} {3}.".format(valor_moeda1,nome_moeda, valor_moeda3, nome_moeda2))
        
print('FIM DO PROGRAMA')