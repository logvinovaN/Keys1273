money = float(input("Введите сумму вклада:"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
bank = per_cent.items()
stavka = list(per_cent.values())
for stavka in per_cent:
    deposite = money / 100.0 * per_cent[stavka]
    for bank in per_cent:
        if stavka == bank:
            print("Deposite",int(deposite),bank)







