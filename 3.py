# Menu de opções
def variavel():
    resposta = -1 

    # estrutura de repetição 
    while resposta != 0:
        print("OPÇÕES:")
        print("1 - SAUDAÇÃO")
        print("2 - BRONCA")
        print("3 - FELICITAÇÃO")
        print("0 - FIM")
        resposta = int(input())  

        if resposta == 1:
            print("1 - Olá. Como vai?")
        elif resposta == 2:
            print("2 - Vamos estudar mais.")
        elif resposta == 3:
            print("3 - Meus Parabéns!")
        elif resposta == 0:
            print("0 - Fim de serviço.")
        else:
            print("Opção inválida.")

# Função principal
def main():
    #saída de dados
    variavel()

# chama a função principal
if __name__ == "__main__":
    main()
