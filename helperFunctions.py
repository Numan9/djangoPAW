def calSum(values):
    total = 0
    for value in values:
        if type(value) != type("-"):
            total += value
    return total