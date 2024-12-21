# Lesson 4:
    # 1st Activity:
number = input("De qual número você quer a tabuada?\n")

print(type(number), number)

number = int(number)

print(type(number), number)

for result in range(number, number * 11, number):
    print(result)

    # 2nd Activity:
total_sum = 0

for num in range(1, 101, 1):
    total_sum += num

print(total_sum)

    # 3rd Activity:
word = input("Digite uma palavra:\n")

for letter in word:
    print(letter)

    # 4th Activity:
for countdown in range(10, 0, -1):
    print(countdown)

print("Feliz Ano Novo!\n")

    # 5th Activity:
even_count = 0
odd_count = 0

print("Digite 10 números:\n")

for _ in range(1, 10, 1):
    number = int(input(""))
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Você digitou {even_count} números pares e {odd_count} números ímpares.")

    # 6th Activity:
even_sum = 0

for number in range(1, 51, 1):
    if number % 2 == 0:
        even_sum += number

print(even_sum)

    # 7th Activity:
import unicodedata

input_word = input("Digite uma palavra:")
vowel_count = 0

normalized_word = unicodedata.normalize("NFD", input_word)
normalized_word = normalized_word.encode("ascii", "ignore")
normalized_word = normalized_word.decode("utf-8")

for letter in normalized_word:
    if letter.lower() in "aeiou":
        vowel_count += 1

if vowel_count > 1:
    print(f"Essa palavra tem {vowel_count} vogais.")
elif vowel_count == 1:
    print(f"Essa palavra tem {vowel_count} vogal.")
else:
    print("Essa palavra não tem vogais.")

    # 8th Activity:
print("---Calculadora de Média---\n")

grades_count = int(input("Quantas notas serão apresentadas?"))

grades_sum = 0.0

for i in range(grades_count):
    grade_number = i + 1
    grade = float(input(f"Insira a {grade_number}° nota:"))
    grades_sum += grade

average = grades_sum / grades_count

if average >= 6:
    print(f"O aluno foi aprovado com média {average}")
else:
    print(f"O aluno foi reprovado com média {average}")

    # 9th Activity:
for num in range(1, 20):
    print(num)
    if num == 15:
        break

    # 10th Activity:
print("Digite até 10 números para serem verificados, digite 0 para parar a verificação antes")

positive_count = 0
negative_count = 0

for _ in range(10):
    number = int(input(""))
    if number != 0:
        if number > 0:
            positive_count += 1
        else:
            negative_count += 1
    else:
        break

print(f"Foram digitados {positive_count} número(s) positivo(s) e {negative_count} número(s) negativo(s)")

    # 11th Activity:
for number in range(1, 31):
    if number % 5 == 0:
        print(f"O número {number} é múltiplo de 5\n")
    elif number > 20:
        break

    # 12th Activity:
print("Digite 5 preços: \n")

total_price = 0

for _ in range(5):
    price = float(input(""))
    total_price += price
    if total_price - (total_price * 0.1) > 100:
        print(f"A soma dos preços com desconto ultrapassou 100 e deu R${total_price - (total_price * 0.1)}")
        break

print(f"A soma dos 5 preços deu {total_price}")
