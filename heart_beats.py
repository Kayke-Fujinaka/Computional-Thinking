def get_sedentary_response():
    while True:
        is_sedentary = input("É sedentário? (sim/não): ").lower()
        if is_sedentary in ['sim', 'não']:
            return is_sedentary == 'sim'
        print("Insira 'sim' ou 'não'.")

def get_bpm(age, is_sedentary=None):
    if age <= 2:
        return "Entre 120 a 140 BPM."
    elif age <= 17:
        return "Entre 80 a 100 BPM."
    elif age >= 18:
        if is_sedentary:
            return "Entre 70 a 80 BPM."
        return "Entre 55 a 70 BPM."

def main():
    age = int(input("Insira uma idade: "))
    is_sedentary = None

    if age >= 18:
        is_sedentary = get_sedentary_response()
        
    print(get_bpm(age, is_sedentary))

if __name__ == "__main__":
    main()