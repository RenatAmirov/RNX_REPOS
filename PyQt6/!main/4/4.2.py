print("""Какой операционной системой вы пользуетесь?
1 — Windows 11
2 — Windows 10
3 — Windows 8.1
4 — Windows 8
5 — Windows 7
6 — Другая""")
os = input("Введите число, соответствующее ответу: ")
if   os == "1":
    print("Вы выбрали: Windows 11")
elif os == "2":
    print("Вы выбрали: Windows 10")
elif os == "3":
    print("Вы выбрали: Windows 8.1")
elif os == "4":
    print("Вы выбрали: Windows 8")
elif os == "5":
    print("Вы выбрали: Windows 7")
elif os == "6":
    print("Вы выбрали: другая")
elif not os:
    print("Вы не ввели число")
else:
    print("Мы не смогли определить вашу операционную систему")
input()
