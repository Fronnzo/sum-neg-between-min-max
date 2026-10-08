"""
Задача: найти сумму отрицательных элементов, расположенных между
максимальным и минимальным элементами одномерного массива.

Автор: Полетаев Константин Валерьевич
"""


def sum_neg_between_min_max(A):
    """
    Возвращает сумму отрицательных элементов между максимумом и минимумом.

    Параметры:
        A — список чисел (int или float)

    Возвращает:
        sum — сумма отрицательных элементов на отрезке между экстремумами.
              Если между ними ничего нет или нет отрицательных — 0.

    Примеры:
        >>> sum_neg_between_min_max([5, -3, 8, -1, -7, 2, -4, 9, -6])
        -4
        >>> sum_neg_between_min_max([10, -2, -5, 3, -8, 1])
        -7
        >>> sum_neg_between_min_max([4, -1, 9, 2, -3])
        0
        >>> sum_neg_between_min_max([1, 5, 3, 2, 4])
        0
    """
    n = len(A)
    if n < 3:
        return 0

    imax = 0
    imin = 0
    for i in range(1, n):
        if A[i] > A[imax]:
            imax = i
        if A[i] < A[imin]:
            imin = i

    left = min(imax, imin) + 1
    right = max(imax, imin) - 1

    total = 0
    for i in range(left, right + 1):
        if A[i] < 0:
            total += A[i]

    return total


def main():
    print("Введите элементы массива через пробел:")
    raw = input().strip()
    if not raw:
        print("Пустой ввод.")
        return

    A = [float(x) if '.' in x else int(x) for x in raw.split()]

    print(f"Массив: {A}")
    print(f"Сумма отрицательных между min и max: {sum_neg_between_min_max(A)}")


if __name__ == "__main__":
    main()