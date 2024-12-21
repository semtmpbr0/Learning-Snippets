#Review
    #1° ACTIVITY

meters = float(input("Insira um tamanho em METROS para ser convertido em CENTIMETROS:"))

centimeters = int(meters * 100)

print(f"O tamanho inserido em centimentros é igual a {centimeters}")

    #2° ACTIVITY

height = float(input("Insira a ALTURA do retângulo em METROS:"))
width = float(input("Insira a LARGURA do retângulo em METROS:"))

area = height * width

print(f"A área do retângulo é igual a {area}m².")

    #3° ACTIVITY

weight = float(input("Insira o seu peso em KG:"))
height = float(input("Insira a sua altura em METROS:"))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print(f"O seu imc é igual a {bmi:.2f} e você está abaixo do peso.")
elif bmi > 29.99:
    print(f"O seu imc é igual a {bmi:.2f} e você está acima do peso.")
else:
    print(f"O seu imc é igual a {bmi:.2f} e você está com o peso normal")

    #4° ACTIVITY

initial_capital = float(input("Insira o capital inicial em REAIS:"))

interest_rate = float(input("Insira a taxa de juros a.a:"))

time_applied = float(input("Insira o tempo aplicado em anos:"))

future_investment = initial_capital * (interest_rate / 100) * time_applied

print(f"O valor futuro do investimento é igual R${future_investment + initial_capital:.2f}")

    #5° ACTIVITY

age = int(input("Insira sua idade em ANOS:"))

if age < 13:
    print("Você é criança.")
elif age < 18:
    print("Você é adolescente.")
elif age < 21:
    print("Você é jovem.")
elif age < 65:
    print("Você é adulto.")
else:
    print("Você é idoso.")

    #6° ACTIVITY

grade = float(input("Insira a sua nota:"))

if grade >= 9:
    print("Sua nota é conceito A.")
elif grade >= 7:
    print("Sua nota é conceito B.")
elif grade >= 5:
    print("Sua nota é conceito C.")
elif grade >= 3:
    print("Sua nota é conceito D.")
elif grade >= 1:
    print("Sua nota é conceito E.")
else:
    print("Sua nota é conceito F.")

    #7° ACTIVITY

username = input("Insira seu login:")
password = input("Insira sua senha:")

attempt = 0
remaining_attempts = 3
print("Redigite a senha para concluir o cadastro(3 tentativas):")
while attempt < 3:
    verification = input("")
    remaining_attempts -= 1
    if verification != password and remaining_attempts == 0:
        print(f"Verificador incorreto.")
    elif verification != password and remaining_attempts != 0:
        print(f"Verificador incorreto, você tem {remaining_attempts} tentativas.")
    else:
        print("Cadastro Concluído.")
        break
    if attempt < 2:
        print("Digite novamente:")
    attempt += 1
else:
    if attempt == 3:
        print(f"Acabou o número de tentativas, cadastro cancelado!")
