print("Farei o cálculo do valor futuro a partir de uma aplicação de juro simples.")
valor_inicial = input("insira o valor com que deseja iniciar.")
taxa_juro = input("Insira a taxa de juro em porcentagem que será aplicada.")
meses = input("Insira a quantia de meses que o juro será aplicado.")
f_valor_inicial = int(valor_inicial)
f_taxa_juro = int(taxa_juro)
f_meses = int(meses)
juro = f_valor_inicial * (f_taxa_juro / 100) * f_meses
resultado = f_valor_inicial + juro
print("O montante foi ", resultado)