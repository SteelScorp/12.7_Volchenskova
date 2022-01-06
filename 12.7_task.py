money = float(input("Какую сумму планируете положить на вклад, ₽:? "))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

deposit = list(per_cent.values())

### Решение с использованием пройденного материала:

# deposit[0] *= money/100
# deposit[1] *= money/100
# deposit[2] *= money/100
# deposit[3] *= money/100

### Решение с использованием цикла-итераций по списку:

for i in range(len(deposit)):
    deposit[i] *= money / 100

print(deposit)
print("Максимальная сумма, которую вы можете заработать: ", max(deposit), "₽")


