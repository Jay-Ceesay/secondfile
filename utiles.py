def find_max(Numbers):
    max = Numbers[0]
    for Number in Numbers:
        if Number > max:
            max = Number
            return max