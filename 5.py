# Calcula a nota e da um conceito.
def notas():          
    resposta = -1    

    # conceitos
    conceito_a = 8.50
    conceito_b = 7.00
    conceito_c = 5.00
    conceito_d = 4.00
    conceito_e = 0.00

    # Estrutura de repetição, é quebrada quando uma nota é valida
    while resposta != 0:
        resposta = float(input("Digite sua nota: "))  
        if resposta < 0 or resposta > 10:       
            print("Nota inválida.") 
        elif resposta >= conceito_a:
            print("Sua nota é: 'A'")
            break
        elif resposta >= conceito_b:
            print("Sua nota é: 'B'") 
            break
        elif resposta >= conceito_c:
            print("Sua nota é: 'C'") 
            break
        elif resposta >= conceito_d:
            print("Sua nota é: 'D'") 
            break
        elif resposta >= conceito_e:
            print("Sua nota é: 'E'")
            break                

# Função principal
def main():
    # Chama a função que faz os cálculos
    notas()

# Executa o programa
if __name__ == "__main__":
    main()
