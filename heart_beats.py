def input_sedentary_status():
    while True:
        is_sedentary = input("É sedentário? (sim/não): ").lower()
        if is_sedentary in ['sim', 'não']:
            return is_sedentary == 'sim'
        print("Insira 'sim' ou 'não'.")

def determine_bpm(age):
    if age <= 2: return "Entre 120 a 140 BPM."
    elif age <= 17: return "Entre 80 a 100 BPM."
    elif 18 <= age < 65:
        is_sedentary = input_sedentary_status()
        return "Entre 70 a 80 BPM." if is_sedentary else "Entre 55 a 70 BPM."
    else: return "Entre 50 a 60 BPM."

def main():
    age = int(input("Insira uma idade: "))
    print(determine_bpm(age))

if __name__ == "__main__":
    main()
