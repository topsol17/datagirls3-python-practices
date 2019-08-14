# #1. total 함수
# #2. average함수
# def total(scores):
#     return scores[0]
#
# def test_total_only_one():
#     assert total([80]) == 80
#     assert total([20]) == 20
#
# def total(scores):
#     return scores[0] + scores[1]
#
# def test_total_with_two_subjects():
#     assert total([80,20]) == 100
#
# def total(scores):
#     total_scores = 0
#     for i in range(0, len(scores)):
#         total_scores += scores[i]
#     return total_scores
#
# def test_total_with_two_subjects():
#     assert total([80,20]) == 100
#
# def test_total_with_large_case():
#     assert total([80,20,60,70,30]) == 260
#
# def test_total_with_empty():
#     assert total([]) == 0
#

def test_list():
    scores = [10,20,30]
    assert scores[1:2] == 20
#append 실험
    scores.append(5)
    assert scores == [10,20,30,5]
#바꾸기
    scores[0] = 0
    assert scores == [0, 10, 20, 5]


def test_dictionary():
    scores = {
        '국어': 10,
        '수학': 20,
        '영어': 30
    }
    assert scores['국어'] == 10
    assert scores['수학'] == 20
    assert scores['영어'] == 30
#새로운것 추가
    scores['미술'] = 40
    assert scores['미술'] == 40

def test_set():
    subjects = {'국어', '수학', '영어'}
    assert '국어' in subjects
    assert '음악' not in subjects
    assert '음악'in subjects.union({'음악'})
#집합과 집합의 결함이라 union 사용
    subjects.add('체육')
    assert '체육' in subjects

# {} 이 괄호는 set, dictionary 에서만 사용
# append, remove, concatenate-> list에서 사용 가능한 것
# union, intersaction, difference -> 집합 사용 가능

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


