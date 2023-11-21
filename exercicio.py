import random #importando a função random

numero_aleatorio = random.randint (1,10000)#chamando randint dentro do random
tentativas = 10#numero de tentativas
print(numero_aleatorio)
for tentativa in range (tentativas):#para chute o numero de tentativas é esse
    print(f'voce tem {tentativas - tentativa} tentativas')
    chute = int(input('digite numero de 1 a 10000:'))
    if chute == numero_aleatorio:  # se chute for diferente de numero sorteado
        print('você acertouu')  # acertouu
        break# pare nao aparece mais
    elif chute < numero_aleatorio:#elif se o numero for < menor que o sorteado
        print('o numero é maior')

    elif chute > numero_aleatorio:#elif se o numero for >maior  que o sorteado
        print('o numero é menor')

else:# acabou as tentativas
    print('acabouuu')
