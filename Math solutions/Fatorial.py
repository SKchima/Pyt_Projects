print ("\n" "Farei o cálculo fatorial de um número de sua escolha!" "\n" "(Deve ser um número natural)")
flagError = True
while flagError:
    valor_de_n = input("Qual o número desejado? ")
    try:
        float_n = float(valor_de_n)
        n = int(valor_de_n)
        p = 1
        componentes = list(range(n, 0, -1))
        for n in componentes:
            p = p * n
        print ("O resultado foi:", p)
        flagError = False
    except:
        print ("caracteres, vírgulas e espaços não são aceitos")