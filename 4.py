# Calcula o total do pedido
def pedido():
    soma = 0.0
    # preços por código
    preco_H = 5.50
    preco_C = 6.80
    preco_M = 4.50
    preco_A = 7.00
    preco_Q = 4.00

    resposta = "" 

    # loop com teste no final: repete até digitar "X"
    while resposta != "X":
        print("CÓDIGO  PRODUTO         PREÇO (R$)")
        print("H       Hamburger       5,50")
        print("C       Cheeseburger    6,80")
        print("M       Misto Quente    4,50")
        print("A       Americano       7,00")
        print("Q       Queijo Prato    4,00")
        print("X       PARA TOTAL DA CONTA")

        resposta = input("Digite uma opção: ").strip().upper()  

        if resposta == "X":
            break  
        elif resposta == "H":
            soma += preco_H   
        elif resposta == "C":
            soma += preco_C
        elif resposta == "M":
            soma += preco_M
        elif resposta == "A":
            soma += preco_A
        elif resposta == "Q":
            soma += preco_Q
        else:
            print("Código inválido")  

    # imprime total final formatado
    print(f"O valor final dos produtos foi: R${soma:.2f}")                          

# Função principal
def main():
    # Chama a função que faz os cálculos
    pedido()

# Executa o programa
if __name__ == "__main__":
    main()
