import math

def eq_segundo_grau(a, b, c, s):
    delta = (b ** 2) - (4 * a * c)
    if delta < 0:
        return("Sem raiz real")
    else:
        valorsqrt = math. sqrt(delta)
        x1 = (- b + valorsqrt) / 2 * a
        x2 = (- b - valorsqrt) / 2 * a
        if s == 1:
            return x1
        else:
             return x2

valorDeA = input("digite o valor de a: ")
valorDeB = input("digite o valor de b: ")
valorDeC = input("digite o valor de c: ")

a = int(valorDeA)
b = int(valorDeB)
c = int(valorDeC)

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