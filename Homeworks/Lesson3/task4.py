def exponentiation(x, y):
    return 1 / x ** abs(y)


print(exponentiation(4, -1))


def exponentiation_version2(x, y):
    if y > 0:
        return 'Введенное значение степени - положительное'
    answer = 1 / x

    for i in range(abs(y + 1)):
        answer *= answer
    return answer


print(exponentiation_version2(4, -1))
