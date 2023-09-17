BONUS_RATE = {
    "Basic": 0.30,
    "Silver": 0.20,
    "Gold": 0.10,
    "Platinum": 0.05
}

def is_valid_subscription_plan(subscription_plan):
  return subscription_plan in BONUS_RATE

def get_annual_billing_from_user():
  try:
    return float(input("Insira o seu faturamento anual: "))
  except ValueError:
    raise ValueError("Por favor, insira um valor válido para o faturamento anual!")

def calculate_bonus(subscription_plan, annual_billing):
  if not is_valid_subscription_plan(subscription_plan):
    raise ValueError("Plano de assinatura inválido!")
  
  return BONUS_RATE[subscription_plan] * annual_billing

def main():
    subscription_plan = input("Insira o seu tipo de assinatura: ")

    try:
      annual_billing = get_annual_billing_from_user()
      bonus = calculate_bonus(subscription_plan, annual_billing)
      print(f"O valor do bônus a ser pago é: R${bonus:.2f}")
    except ValueError as error_message:
      print(error_message)

if __name__ == "__main__":
    main()
