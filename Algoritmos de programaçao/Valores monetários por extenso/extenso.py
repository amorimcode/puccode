'''

'''
print("PROGRAMA PARA ESCREVER POR EXTENSO VALORES ENTRE R$-999,99 E R$999,99\n")

try:
    valor = float(input("Digite o valor desejado: "))  # -3.758437

    if valor < -999.99 or valor > 999.99:
        print("Valor fora da faixa solicitada!")
    else:
        # testa valor negativo
        if valor < 0:
            negativo = True
            valor = -valor  # 3.758437
        else:
            negativo = False

        if valor == 0:
            print("zero reais")
        else:
            reais = int(valor)  # 3
            fracao = valor-reais  # 0.758437
            fracao *= 100  # 75.8437
            centavos = int(fracao)  # 75
            fracao -= centavos  # 0.8437
            if fracao != 0:
                print("Foram digitados centavos com mais de dois dígitos")
            else:
                '''
                if not negativo: # if negativo==False:
                '''
                if negativo:  # if negativo==True:
                    print("menos ", end="")

                if reais == 0:
                    print("zero ", end="")
                elif reais == 1:
                    print("um ", end="")
                elif reais == 2:
                    print("dois ", end="")
                elif reais == 3:
                    print("três ", end="")
                elif reais == 4:
                    print("quatro ", end="")
                elif reais == 5:
                    print("cinco ", end="")
                elif reais == 6:
                    print("seis ", end="")
                elif reais == 7:
                    print("sete ", end="")
                elif reais == 8:
                    print("oito ", end="")
                elif reais == 9:
                    print("nove ", end="")
                    

                if reais == 1:
                    print("real ", end="")
                else:
                    print("reais ", end="")

                if centavos != 0:
                    print("e ", end="")

                dezena = centavos//10  # 7
                unidade = centavos % 10  # 5

                if dezena == 1:
                    if unidade == 0:
                        print("dez ", end="")
                    elif unidade == 1:
                        print("onze ", end="")
                    elif unidade == 2:
                        print("doze ", end="")
                    elif unidade == 3:
                        print("treze ", end="")
                    elif unidade == 4:
                        print("quatorze ", end="")
                    elif unidade == 5:
                        print("quinze ", end="")
                    elif unidade == 6:
                        print("dezesseis ", end="")
                    elif unidade == 7:
                        print("dezessete ", end="")
                    elif unidade == 8:
                        print("dezoito ", end="")
                    elif unidade == 9:
                        print("dezenove ", end="")
                elif dezena == 2:
                    print("vinte ", end="")
                elif dezena == 3:
                    print("trinta ", end="")
                elif dezena == 4:
                    print("quarenta ", end="")
                elif dezena == 5:
                    print("cinquenta ", end="")
                elif dezena == 6:
                    print("sessenta ", end="")
                elif dezena == 7:
                    print("setenta ", end="")
                elif dezena == 8:
                    print("oitenta ", end="")
                elif dezena == 9:
                    print("noventa ", end="")

                if dezena >= 2 and unidade != 0:
                    print("e ", end="")

                if dezena > 1:
                    if unidade == 1:
                        print("um ", end="")
                    elif unidade == 2:
                        print("dois ", end="")
                    elif unidade == 3:
                        print("três ", end="")
                    elif unidade == 4:
                        print("quatro ", end="")
                    elif unidade == 5:
                        print("cinco ", end="")
                    elif unidade == 6:
                        print("seis ", end="")
                    elif unidade == 7:
                        print("sete ", end="")
                    elif unidade == 8:
                        print("oito ", end="")
                    elif unidade == 9:
                        print("nove ", end="")

                if centavos == 1:
                    print("centavo")
                else:
                    if centavos != 0:
                        print("centavos")

except ValueError:
    print("Valores monetários não devem conter letras ou outros caracteres não numéricos!")

print("\n\nOBRIGADO POR USAR ESTE PROGRAMA!")
