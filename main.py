# Программа конвертирует сумму по курсу с учётом комиссии.
# Входные данные: amount - сумма, rate - курс, commission - комиссия в %.
# Формула: amount * rate * (1 - commission / 100).

amount = float(input("Введите сумму: "))
rate = float(input('Введите курс: '))
commission = float(input('Введите комиссию в %: '))

result = amount * rate * (1 - commission / 100)

print(f'Итоговая сумма {result:.2f}')