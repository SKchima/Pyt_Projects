print ("Farei a multiplicação dos componentes de uma progressão geométrica de sua escolha, começando por 1!")
flag_error = True
while flag_error:
    print ("Caso queira sair, envie N maiúsculo em pelo menos uma das respostas.")
    razao = input("Qual a razão da PG? ")
    numero = input("Quantos números possui essa PG? ")
    try:
        if (razao == ("N") or numero == ("N")):
            flag_error = False
        else:
            float_razao = float(razao)
            int_numero = int(numero)
            resultado = (1 * ((float_razao ** int_numero) - 1)) / (float_razao - 1)
            #componentes = range(1, int_numero, 1)
            #p = 0
            #n = 0
            #for float_numero in componentes:
            #    n = n + 1
            #    p = 1 + p * (float_razao * n)
            print ("O resultado foi:", resultado)
            flag_error = False
    except:
        print ("\n" "caracteres, vírgulas e espaços não são aceitos")