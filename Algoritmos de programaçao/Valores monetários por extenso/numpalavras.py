# precisa instalar a biblioteca num2words
# pip install num2words

from num2words import num2words
try:
    class num2words:

        numberInputed = float(input('Digite o valor desejado: '))

        if numberInputed < 0:
            print("menos ", end="")
            number_p = numberInputed * -1

        else:
            number_p = numberInputed

        if float(number_p) < -999.99 or float(number_p) > 999.99:
            print("Valor fora da faixa solicitada!")
        elif number_p == 0:
            print('zero real')
        else:
            def number_to_long_number(number_p):
                    
                        number_p = str(number_p)
                        if number_p.find('.') != -1:
                            number_p = number_p.split('.')
                            number_p1 = int(number_p[0].replace('.', ''))
                            number_p2 = int(number_p[1])
                        else:
                            number_p1 = int(number_p.replace('.', ''))
                            number_p2 = 0

                        if number_p1 == 1:
                            aux1 = ' real'
                        else:
                            aux1 = ' reais'

                        if number_p2 == 1:
                            aux2 = ' centavo'
                        else:
                            aux2 = ' centavos'

                        text1 = ''
                        if number_p1 > 0:
                            text1 = num2words(number_p1, lang='pt_BR') + str(aux1)
                        else:
                            text1 = ''

                        if number_p2 > 0:
                            text2 = num2words(number_p2, lang='pt_BR') + str(aux2)
                        else:
                            text2 = ''

                        if (number_p1 > 0 and number_p2 > 0):
                            result = text1 + ' e ' + text2
                        else:
                            result = text1 + text2

                        print(result)
                    

            if int(number_p) < 0:
                print('menos ', end='')


            number_to_long_number(number_p)
except ValueError:
    print("Valores monetários não devem conter letras ou outros caracteres não numéricos!")

print("\nOBRIGADO POR USAR ESTE PROGRAMA!")
