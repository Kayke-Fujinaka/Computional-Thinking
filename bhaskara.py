import math

def calculate_delta(a, b, c):
  return b * b - 4 * a * c

def calculate_actual_values(a, b, delta):
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    return x1, x2

def main ():
  a = float(input("Informe o valor de A: "))
  b = float(input("Informe o valor de B: "))
  c = float(input("Informe o valor de C: "))

  delta = calculate_delta(a, b, c)

  if (delta < 0.0):
    print ("Para a equação {}x² + {}x + {} = 0, não existem valores reais para x".format(a, b, c))
  elif (delta == 0):
    x = calculate_actual_values(a, b, delta)
    print ("Para a equação {}x² + {}x + {} = 0, obtivemos o seguinte valor: x = {}".format(a, b, c, x))
  else:
    x1, x2 = calculate_actual_values(a, b, delta)
    print ("Para a equação {}x² + {}x + {} = 0, obtivemos os seguintes valores: x1 = {} e x2 = {}".format(a, b, c, x1, x2))
    
if __name__ == "__main__":
    main()