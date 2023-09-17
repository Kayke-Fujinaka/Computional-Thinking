def main():
  response = input("Qual é a resposta para a vida, o universo e tudo mais? ")
  
  while response != "42":
    response = input("Qual é a resposta para a vida, o universo e tudo mais? ")
  
if __name__ == "__main__":
  main()
  print("Parabéns, você acertou!")