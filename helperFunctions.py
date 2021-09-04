def calSum(values):
    total = 0
    for value in values:
        if value and type(value) != type("-"):
            total += value
    return total