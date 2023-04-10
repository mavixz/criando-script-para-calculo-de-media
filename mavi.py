#Pedindo nome
nome = input ("Digite seu nome: ")

# Pedindo as notas
p1 = float( input("Digite a nota de P1: ") )
p2 = float( input("Digite a nota do P2: ") )

# Cálculo da média
media = (p1 + p2) / 2
print(f"media: {media}")

if media >= 7.5:
    result ="Aprovado"
elif media < 6:
    result = "Reprovado"
elif media < 7 and media > 6: 
    result = "Recuperação!"
else:
    print ("insira um valor valido")

print(f"\nnome: {nome} \nmedia: {media: .2f} \nStatus: {result}")
#teste
