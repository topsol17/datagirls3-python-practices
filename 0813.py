#class_total
#class_total_all

class_scores = [
    {
        '국어': 80,
        '영어': 100,
        '수학': 50
    },
    {
        '국어': 90,
        '영어': 70,
        '수학': 40
    }
]

def class_total(class_scores, subject):
    # results = {
    #     0: 0,
    #     1: 100
    # }
    # return results[len(class_scores)]
    total_score = 0
    # 누산
    for i in range(len(class_scores)):
        scores = class_scores[i]
        total_score += scores[subject]
        # total_score += scores.get(subject, 0)
    return total_score


def class_total_all(class_scores):
    total_score = 0
    # for i in range(len(class_scores)):
    #     total_score += total_all(class_scores[i])
    for scores in class_scores:
        total_score += total_all(scores)
    return total_score


def total_all(scores):
    total_score = 0
    for i in scores:
        total_score += scores[i]
    # for score in scores.values():
    #     total_score += score
    # weights = {'국어': 2, '영어': 1}
    # for k, v in scores.items():
    #     total_score += v * weights[k]
    return total_score


def test_class_total():
    assert class_total([], '국어') == 0
    assert class_total([{'국어': 100}], '국어') == 100
    assert class_total([{'국어': 100}, {'국어': 30}], '국어') == 130
    assert class_total([
        {'국어': 100}, {'국어': 30}, {'국어': 80}
    ], '국어') == 210
    assert class_total([
        {'국어': 100, '영어': 100},
        {'국어': 30, '영어': 10},
        {'국어': 80, '영어': 80}
    ], '국어') == 210
    assert class_total([
        {'국어': 100, '영어': 100},
        {'국어': 30, '영어': 10},
        {'국어': 80, '영어': 80}
    ], '영어') == 190
    # assert class_total([
    #     {'국어': 100, '영어': 100},
    #     {'국어': 30, '영어': 10},
    #     {'국어': 80, '영어': 80}
    # ], '수학') == 0


def test_class_total_all():
    assert class_total_all([]) == 0
    assert class_total_all([{'국어': 100}]) == 100
    assert class_total_all([{'국어': 100, '영어': 100}]) == 200
    assert class_total_all([
        {'국어': 100, '영어': 100},
        {'국어': 30, '영어': 10},
        {'국어': 80, '영어': 80}
    ]) == 400


def test_total_all():
    assert total_all({'국어': 100}) == 100
    assert total_all({'국어': 100, '영어': 10}) == 110
    assert total_all({'국어': 100, '영어': 10, '수학': 90}) == 200
