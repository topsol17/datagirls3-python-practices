# assert 1 + 1 == 2
# assert 1 + 2 == 3
#
# def double(n):
#     return n*2
# assert double(2) == 4
# assert double(3) == 6
#
#
# def test_double():
#     assert double(2) == 4
#     assert double(1) == 2

scores = [80,100,70,90,40]

def total(something):
    total_scores = 0
    for i in something:
        total_scores += i
    return total_scores

def test_total():
    assert total(scores) == 380

scores = [80,100,70,90,40]

def average(something):
    total_scores = 0
    for i in something:
        total_scores += i
    return total_scores / len(something)

def test_average():
    assert average(scores) == 76
