def check_answer(selected_option):
    if selected_option == 'b':
        return "Correto!"
    else:
        return "Errado. Tente novamente."

print("Selecione a alternativa que apresenta uma expressão que retorne True para uma nota válida. Considere como válido os valores de 0 a 10, inclusive.")
print("a) nota > 0 and nota < 10")
print("b) nota >= 0 and nota <= 10")
print("c) nota > 0 or nota < 10")
print("d) nota => 0 or nota <= 10")

answer = input("Escolha uma alternativa (a, b, c, d): ")

feedback = check_answer(answer)
print(feedback)
