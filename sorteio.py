from random import randint
pc = randint(0, 5)
print("Qual numero escolhi de 0 a 5 ?")
jogador = int(input("Qual numero pensei\n"))
if jogador == pc:
    print("Voce conseguiu !!!")
else:
    print("Voce nao conseguiu eu pensei no numero {} e nao no {}".format(pc, jogador))
