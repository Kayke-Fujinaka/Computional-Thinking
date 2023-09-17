TOTAL_STUDENTS = 50
HALF_STUDENTS = TOTAL_STUDENTS // 2
MIN_GRADE = 0
MAX_GRADE = 10


def get_student_grade(student_number):
    while True:
        try:
            grade = float(
                input(f"POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {student_number}: "))
            if MIN_GRADE <= grade <= MAX_GRADE:
                return grade
            else:
                print(
                    f"Por favor, insira uma nota válida entre {MIN_GRADE} e {MAX_GRADE}.")
        except ValueError:
            print("Por favor, insira um valor numérico válido para a nota.")


def collect_grades(start, step):
    total_grade = 0
    for student_number in range(start, TOTAL_STUDENTS + 1, step):
        total_grade += get_student_grade(student_number)
    return total_grade / HALF_STUDENTS


def determine_highest_average(odd_avg, even_avg):
    if odd_avg > even_avg:
        return "A média dos alunos ímpares é maior."
    elif odd_avg < even_avg:
        return "A média dos alunos pares é maior."
    return "As médias dos alunos ímpares e pares são iguais."


def main():
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES.")
    average_odd_students = collect_grades(1, 2)

    print("\nVOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES.")
    average_even_students = collect_grades(2, 2)

    result = determine_highest_average(
        average_odd_students, average_even_students)
    print(result)


if __name__ == "__main__":
    main()
