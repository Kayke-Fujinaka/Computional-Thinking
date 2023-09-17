def main():
  students = int(input("Insira o total de alunos: "))
  
  votes = {
        "Monday": 0,
        "Tuesday": 0,
        "Wednesday": 0,
        "Thursday": 0,
        "Friday": 0
  }
  
  for _ in range(1, students + 1):
    vote = input("Escolha o dia da semana: ")
    if(vote == "Monday"): votes["Monday"]+= 1
    elif(vote == "Tuesday"): votes["Tuesday"]+= 1
    elif(vote == "Wednesday"): votes["Wednesday"]+= 1
    elif(vote == "Thursday"): votes["Thursday"]+= 1
    elif(vote == "Friday"): votes["Friday"]+= 1
    
  max_votes = max(votes.values())
  
  chosen_days = []
  
  for day, vote_count in votes.items():
    if vote_count == max_votes:
        chosen_days.append(day)

  print(f"O dia escolhido foi {chosen_days[0]} com {max_votes} de {students} votos.")
    
if __name__ == "__main__":
  main()