def input_sedentary_status():
    while True:
        is_sedentary = input("É sedentário? (sim/não): ").lower()
        if is_sedentary == 'sim':
            return True
        elif is_sedentary == 'não':
            return False
        print("Insira 'sim' ou 'não'.")

def determine_bpm(age, is_sedentary=False):
    if age <= 2:
        return "Entre 120 a 140 BPM."
    elif age <= 17:
        return "Entre 80 a 100 BPM."
    elif age >= 65:
        return "Entre 50 a 60 BPM."
    elif is_sedentary:
        return "Entre 70 a 80 BPM."
    else:
        return "Entre 55 a 70 BPM."

def main():
    age = int(input("Insira uma idade: "))
    
    if age >= 18 and age < 65:
        is_sedentary = input_sedentary_status()
        print(determine_bpm(age, is_sedentary))
    else:
        print(determine_bpm(age))

if __name__ == "__main__":
    main()
