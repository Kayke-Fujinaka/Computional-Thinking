def initialize_vote_counts():
    return {
        "Segunda-feira": 0,
        "Terça-feira": 0,
        "Quarta-feira": 0,
        "Quinta-feira": 0,
        "Sexta-feira": 0
    }

def collect_student_votes(students, votes):
    for _ in range(students):
        while True:
            student_vote = input(
                "Escolha o dia da semana (Segunda-feira, Terça-feira, Quarta-feira, Quinta-feira e Sexta-feira): ")
            if student_vote in votes:
                votes[student_vote] += 1
                break
            else:
                print("Dia inválido! Tente novamente.")

def get_most_voted_day(votes):
    highest_vote_count = max(votes.values())

    chosen_days = [day for day, vote_count in votes.items()
                   if vote_count == highest_vote_count]

    return [highest_vote_count, chosen_days]

def display_result(highest_vote_count, chosen_days, total_students):
    if total_students == 0:
        print("Nenhum voto foi registrado.")
        return
    
    if len(chosen_days) == 1:
        print(
            f"O dia escolhido foi {chosen_days[0]} com {highest_vote_count} de {total_students} votos.")
    else:
        days = ', '.join(chosen_days)
        print(
            f"Houve um empate entre os dias {days} com {highest_vote_count} votos cada.")

def main():
    try:
        students = int(input("Insira o total de alunos: "))

        votes = initialize_vote_counts()
        collect_student_votes(students, votes)

        highest_vote_count, chosen_days = get_most_voted_day(votes)
        display_result(highest_vote_count, chosen_days, students)

    except ValueError:
        print("Por favor, insira um número inteiro válido para o total de alunos.")

if __name__ == "__main__":
    main()
