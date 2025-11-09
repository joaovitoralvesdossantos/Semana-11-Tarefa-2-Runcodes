# Calcula a idade das pessoas
def idade():
    contador = 0     
    soma = 0        
    resposta = -1    
    menor = None     
    maior = None    

    # mensagens na tela
    print("Digite uma idade")
    print("Utilize '0' para finalizar a lista!")

    # Estrutura de repetição com teste no final
    while resposta != 0:
        resposta = int(input("Idade: "))  
        if resposta == 0:       
            break
        if menor is None or resposta < menor:  
            menor = resposta
        if maior is None or resposta > maior:  
            maior = resposta 
        contador += 1         
        soma += resposta       

    # Calcula e mostra os resultados se tiver pelo menos uma idade
    if contador > 0:
        media = soma / contador             
        print(f"Número de pessoas: {contador}")                    
        print(f"A média de idade das pessoas: {media:.2f}")               
        print(f"A menor idade foi: {menor}")                      
        print(f"A maior idade foi: {maior}")                       

# Função principal
def main():
    # Chama a função que faz os cálculos
    idade()

# Executa o programa
if __name__ == "__main__":
    main()
