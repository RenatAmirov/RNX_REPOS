def summa(a, b, c):
    return a + b + c

seq1 = [1, 2, 3]
print(summa(*seq1))                # Распаковка списка
seq2 = (2, 3)
print(summa(1, *seq2))             # Можно совмещать указание
                                   # обычных параметров и распаковку
mpn1 = {"a": 1, "b": 2, "c": 3}
print(summa(**mpn1))               # Распаковка словаря
seq3, mpn2 = (1, 2), {"c": 3}
print(summa(*seq3, **mpn2))        # Можно совмещать распаковку
                                   # списков и словарей
