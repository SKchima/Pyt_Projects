print ("\n" "Farei o cálculo fatorial de um número de sua escolha!" "\n" "(Deve ser um número natural)")
flag_error = True
while flag_error:
    print ("Caso queira sair, envie N")
    valor_de_n = input("Qual o número desejado? ")
    try:
        if valor_de_n == ("N"):
            flag_error = False
        else:
            n = int(valor_de_n)
            p = 1
            components = list(range(n, 0, -1))
            for n in components:
                p = p * n
            print ("O resultado foi:", p)
            flag_error = False
    except:
        print ("\n" "caracteres, vírgulas e espaços não são aceitos")