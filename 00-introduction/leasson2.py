# Lesson 2:
    # 1st Activity:
print("Calculadora de Salário\n")

hourly_rate = float(input("Quanto você recebe por hora trabalhada?\n"))
worked_hours = float(input("Quantas horas você trabalhou esse mês?\n"))

gross_salary = hourly_rate * worked_hours

income_tax = gross_salary * 0.11
social_security = gross_salary * 0.08
union_dues = gross_salary * 0.05
total_deductions = gross_salary * 0.24
net_salary = gross_salary - total_deductions

print(f"Salário Bruto : R$ {gross_salary}")
print(f"IR (11%) : R$ {income_tax}")
print(f"Sindicato (5%) : R$ {union_dues}")
print(f"Salário Líquido : R$ {net_salary}")

    # 2nd Activity:
num1 = int(input("Insira o primeiro número:\n"))
num2 = int(input("Insira o segundo número:\n"))

if num1 > num2:
    print("O primeiro número é o maior.\n")
elif num2 > num1:
    print("O segundo número é o maior.\n")
else:
    print("Os números são iguais.\n")

    # 3rd Activity:
number = float(input("Insira um número:\n"))

if number > 0:
    print("O número é positivo.\n")
elif number < 0:
    print("O número é negativo.\n")
else:
    print("O número é 0.\n")

    # 4th Activity:
gender = input("Você é de qual gênero? (M/F/N)\n")

if gender == "F" or gender == "f":
    print("F - Feminino\n")
elif gender == "M" or gender == "m":
    print("M - Masculino\n")
elif gender == "N" or gender == "n":
    print("N - Neutro\n")
else:
    print(f"{gender} está inválido\n")

    # 5th Activity:
num1 = float(input("Digite o primeiro número: \n"))
num2 = float(input("Digite o segundo número: \n"))
num3 = float(input("Digite o terceiro número: \n"))

if num1 > num2 and num1 > num3:
    if num2 > num3:
        print(f"{num1} {num2} {num3}")
    else:
        print(f"{num1} {num3} {num2}")
elif num2 > num1 and num2 > num3:
    if num1 > num3:
        print(f"{num2} {num1} {num3}")
    else:
        print(f"{num2} {num3} {num1}")
else:
    if num1 > num2:
        print(f"{num3} {num1} {num2}")
    else:
        print(f"{num3} {num2} {num1}")

    # 6th Activity:
grade1 = float(input("Qual é a primeira nota parcial do aluno?\n"))
grade2 = float(input("Qual é a segunda nota parcial do aluno?\n"))
average = (grade1 + grade2) / 2

if average == 10:
    print(f"Aprovado com distinção! Média: {average}")
elif average >= 7:
    print(f"Aprovado! Média: {average}")
else:
    print(f"Reprovado! Média: {average}")

    # 7th Activity:
vowels = ["a", "e", "i", "o", "u"]
consonants = [
    "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", 
    "p", "q", "r", "s", "t", "v", "w", "y", "z"
]

letter = input("Insira uma letra:\n")
letter = letter.lower()

if letter in vowels:
    print("Essa letra é uma vogal.\n")
elif letter in consonants:
    print("Essa letra é uma consoante.\n")
else:
    print("Dado inválido")
