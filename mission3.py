# Missão 3:  Recuperando o Sistema de Notas 

nota = float(input("Digite a nota do aluno: "))


if 90 <= nota <= 100:
    print("Parabéns, você tirou A!")
elif 80 <= nota <= 89:
    print("Muito bem, você tirou B.")
elif 70 <= nota <= 79:
    print("Bom trabalho, você tirou C.")
elif 60 <= nota <= 69:
    print("Fique atento, você tirou D.")
else:
    print("Estude um pouco mais, você tirou F.")

input("\nPressione Enter para sair...")