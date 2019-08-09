scores = [80, 100, 70, 90, 40]


def total(scores):
    total_score= 0
    for i in range(0, len(scores)):
        total_score += scores[i]
    return total_score

print (total(scores))

