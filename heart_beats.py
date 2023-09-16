age = int(input("Insira uma idade: "))

if age <= 2:
    print("Entre 120 a 140 BPM.")
elif age <= 17:
    print("Entre 80 a 100 BPM.")
elif age >= 18:
    is_sedentary = input("É sedentário? (sim/não): ").lower()
    
    while is_sedentary not in ['sim', 'não']:
        print("Insira 'sim' ou 'não'.")
        is_sedentary = input("É sedentário? (sim/não): ").lower()
      
    if is_sedentary == 'sim':
        print("Entre 70 a 80 BPM.")
    else:
        print("Entre 55 a 70 BPM.")
else:
    print("Entre 50 a 60 BPM.")
  
print()
