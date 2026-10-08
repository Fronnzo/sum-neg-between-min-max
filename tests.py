"""
Тесты для функции sum_neg_between_min_max.
Запуск: python tests.py
"""

from solution import sum_neg_between_min_max


def run_test(name, A, expected):
    result = sum_neg_between_min_max(A)
    status = "OK" if result == expected else "FAIL"
    print(f"[{status}] {name}: получено {result}, ожидалось {expected}")
    return result == expected


def main():
    tests = [
        ("Базовый пример",       [5, -3, 8, -1, -7, 2, -4, 9, -6], -4),
        ("Максимум левее",       [10, -2, -5, 3, -8, 1],             -7),
        ("Экстремумы рядом",     [4, -1, 9, 2, -3],                   0),
        ("Все положительные",    [1, 5, 3, 2, 4],                     0),
        ("Все отрицательные",    [-5, -3, -8, -1, -7],               -4),  # между -8 и -1? см. ниже
        ("Один элемент",         [42],                                 0),
        ("Два элемента",         [1, 2],                               0),
        ("Пустой массив",        [],                                   0),
        ("Отрицательных нет",    [-1, 5, 10, 3, -2],                   5),
        ("Несколько минимумов",  [3, -5, 1, -5, 7, -2],                0),
    ]

    passed = 0
    for name, A, expected in tests:
        if run_test(name, A, expected):
            passed += 1

    print(f"\nПройдено {passed} из {len(tests)}")


if __name__ == "__main__":
    main()