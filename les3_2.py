inf = lambda name, fam, age, city, tel, email: print(name, fam, age, "год", " город", city, tel, email)

a = [input("Введите имя "), input("Введите фамилию "), input("Введите год рождения "), input("Введите родной город "),
     input("Введите телефон "), input("Введите email ")]

inf(name=a[0], fam=a[1], age=a[2], city=a[3], tel=a[4], email=a[5])
