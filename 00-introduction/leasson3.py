# Lesson 3:
    # 1st Activity:
counter = 0
n = 2

while counter < 5:
    print(n, "\n")
    n += 2
    counter += 1

print("Fim da contagem!") 

    # 2nd Activity:
counter = 0
n = 0

while counter < 10:
    n += 1
    if n % 2 == 0:
        print(n, "\n")
    counter += 1

print("Fim da contagem!")

    # 3rd Activity:
secret_number = 15
attempt = 0

while attempt != secret_number:
    attempt = int(input("Qual é o número secreto?\n"))
    if attempt > secret_number:
        print("Errouu! dica: O número secreto é menor que o número digitado.\n")
    elif attempt < secret_number:
        print("Errouu! dica: O número secreto é maior que o número digitado.\n")
    else:
        print("Acertouuu!")

    # 4th Activity:
secret_number = 36
attempts = 0

print("Adivinhe um número de 1 a 100 em até 5 tentativas\n")

while attempts < 5:
    guess = int(input("Qual é o número secreto?\n"))
    if guess > secret_number:
        print("Errouu! dica: O número secreto é menor que o número digitado.\n")
    elif guess < secret_number:
        print("Errouu! dica: O número secreto é maior que o número digitado.\n")
    else:
        print("Acertouuu!")
        break
    attempts += 1
else:
    if attempts == 5:
        print(f"Acabou o número de tentativas! O número era {secret_number}")

    # 5th Activity:
total_sum = 0
even_numbers = []

while total_sum < 50:
    number = int(input("Digite um número inteiro:\n"))
    if number % 2 == 0:
        total_sum += number
        even_numbers.append(number)

i = 0

print("A soma dos números pares digitados foi:\n")

while i < len(even_numbers) - 1:
    print(f"{even_numbers[i]}+", end="")
    i += 1

print(even_numbers[i], end="")
print(f"={total_sum}")
