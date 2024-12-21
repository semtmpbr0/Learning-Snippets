# Lesson 1:
    # 1st Activity:
num1 = int(input("Qual é o primeiro número?\n"))
num2 = int(input("Qual é o segundo número?\n"))
result = num1 + num2
print(f"O resultado da soma é {result}\n")

    # 2nd Activity:
grade1 = float(input("Insira a primeira nota: \n"))
grade2 = float(input("Insira a segunda nota: \n"))
grade3 = float(input("Insira a terceira nota: \n"))
grade4 = float(input("Insira a quarta nota: \n"))
average = (grade1 + grade2 + grade3 + grade4) / 4
print(f"A média do aluno foi: {average}")

    # 3rd Activity:
meters = float(input("Quantos metros você quer que sejam convertidos?\n"))
centimeters = int(meters * 100)
print(f"Essa distância dá {centimeters} centímetros\n")

    # 4th Activity:
side_length = float(input("Quanto mede o lado do quadrado?\n"))
area = int(side_length ** 2)
double_area = area * 2
print(f"A área desse quadrado é {area} e o dobro dela é {double_area}\n")

    # 5th Activity:
worked_hours = int(input("Quantas horas você trabalhou esse mês?\n"))
hourly_rate = float(input("Quanto você recebe por hora?\n"))
salary = float(hourly_rate * worked_hours)
print(f"Você receberá R${salary} esse mês\n")