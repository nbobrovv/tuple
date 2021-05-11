#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    # Ввести список одной строкой.
    a = tuple(map(float, input("Введите кортеж --> ").split()))
    c = float(input('Введите c: '))
    # Переменная k для дальнейших вычислений после отрицательного элемента
    k = 0
    # Если список пуст, завершить программу.
    if not a:
        print("Заданный кортеж пуст", file=sys.stderr)
        exit(1)
    # Вывод меньших элементов
    s = 0
    for i in a:
        if i < c:
            s += 1
    # Сумма после отрицательных элементов
    n_0 = len(a)
    for i, item in reversed(tuple(enumerate(a))):
        if item < 0:
            n_0 = i
            break
    for z in a:
        k = sum(a[n_0 + 1:])
    # Сортировка элементов (от большего к меньшему)
    f = str(tuple(sorted(a, key=lambda x: abs(x-max(a)))))
    print("Количество элементов кортежа, меньших с --> ", s)
    print("Сумма после отрицательных элементов -- > ", k)
    print("Упорядоченный кортеж --> ", f)