def calculate_factorial(minutes):
    if minutes == 0:
        return 1

    result = 1
    for i in range(1, minutes + 1):
        result *= i

    return result


def generate_unlock_password(minutes):
    return "LIBERDADE" + str(calculate_factorial(minutes))


def is_valid_minutes(minutes):
    return 0 <= minutes <= 59


def main():
    try:
        minutes = int(input("Insira os minutos atuais (0 a 59): "))

        if is_valid_minutes(minutes):
            password = generate_unlock_password(minutes)
            print(f"A senha para desbloqueio é: {password}")
        else:
            print("Por favor, insira um minuto válido entre 0 e 59.")

    except ValueError:
        print("Por favor, insira um número válido para os minutos.")


if __name__ == "__main__":
    main()
