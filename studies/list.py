jedis = ["Yoda", "Luke", "Obi-Wan", "Anakin"]

# Inserir em uma posição específica
jedis.insert(2, "Ahsoka")

# Adicionar no final
jedis.append(input("Digite o nome de um jedi: "))

# Remover o último valor
jedis.pop()

# Remover uma posição específica
jedis.pop(2)

# Remover valor específico
jedis.remove("Yoda")

# Exibir lista
print("A lista foi criada assim: {}".format(jedis))

# Contar elementos
print("O total de jedis é {}".format(jedis.count("Anakin")))

# Inverter lista
jedis.reverse()
print("A lista agora está invertida: {}".format(jedis))

# Ordenar lista
jedis.sort()
print("A lista agora está ordenada: {}".format(jedis))

# Tamanho da lista
length = len(jedis)
print("A lista tem {} elementos".format(length))
