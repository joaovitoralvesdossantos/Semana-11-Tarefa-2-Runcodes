# Faz a soma dos numeros inteiros
def conjuto():
    contador = 0           
    resposta = -1   

    # mensagens na tela
    print("Digite um número")
    print("Utilize '0' para finalizar a soma dos números digitados!")

    # Estrutura de repetição com teste no final
    while resposta != 0:
        resposta = int(input("Número: "))  
        if resposta == 0:       
            break
        contador += + resposta             

    # Calcula e mostra os resultados se tiver pelo menos um número inteiro
    if contador > 0:            
        print(f"A soma dos números é: {contador}")                                                     
    else:
        print (f"0")
# Função principal
def main():
    # Chama a função que faz os cálculos
    conjuto()

# Executa o programa
if __name__ == "__main__":
    main()
