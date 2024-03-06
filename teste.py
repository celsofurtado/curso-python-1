if __name__ == "__main__":
    print("esse é o main!!!")

nome = "João Silva"
telefone = "11 9999-9999"
email = "joao.silva@email.com"

print(f"{nome:<15}{telefone:<15}{email:<15}")

valores = [1, 2, 3]
print(valores)
valores.insert(1, 100)
print(valores)
valores.remove(3)
print(valores)

try:
    valores.remove(100)
except:
    print("O valor fornecido não existe")

print(valores)
valores.append(18)
valores.append(11)
print(valores)

valores.pop(2)
print(valores)
try:
    valores.pop(10)
except:
    print("Índice não existe")

frutas = input("Lista de frutas:\n").split(",")

print(frutas)

