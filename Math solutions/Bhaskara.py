import math

def eq_segundo_grau(a, b, c, s):
    delta = (b ** 2) - (4 * a * c)
    if delta < 0:
        return("Sem raiz real")
    else:
        valor_sqrt = math. sqrt(delta)
        x1 = (- b + valor_sqrt) / 2 * a
        x2 = (- b - valor_sqrt) / 2 * a
        if s == 1:
            return x1
        else:
            return x2

flag_error = True
while flag_error:
    print ("\n" "Caso queira sair, envie N maiúsculo em pelo menos uma das respostas.")
    valor_de_a = input("Digite o valor de a: ")
    valor_de_b = input("Digite o valor de b: ")
    valor_de_c = input("Digite o valor de c: ")
    try:
        if (valor_de_a == ("N") or valor_de_b == ("N") or valor_de_c == ("N")):
            flag_error = False
        else:
            a = int(valor_de_a)
            b = int(valor_de_b)
            c = int(valor_de_c)

            x1 = eq_segundo_grau(a, b, c, 1)
            x2 = eq_segundo_grau(a, b, c, 2)

            if x1 == "Sem raiz real":
                print ("Sem raiz real")
            else:
                if x1 == x2:
                    print ("Ambas as raízes são =", x1)
                else:
                    print ("x1 =", x1)
                    print ("x2 =", x2)
    except:
        print ("\n" "caracteres, vírgulas e espaços não são aceitos")