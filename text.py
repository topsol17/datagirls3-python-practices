# scores = [80, 100, 70, 90,40]
#
# sum = 0
#
# for num in scores :
#     sum += num
#
# print ('test1:', sum)
#
#
# sum = 0
#
# for y in [8*10, 100, 70, 90, 40]:
#     sum = sum + y
#
# print ('test2:', sum)
#
#
#
# for num in [80, 100, 70, 90, 40]:
#     sum = 0
#     sum += num
#
# print ('test3:', sum)
#
#
gugu = 1
sum = 0
for x in range(1, 10):
    for y in range(1, 10):
        gugu = x * y
        print('test4', gugu)
        sum += gugu
print(sum)

import statistics

sum = 0
my_scores = [30, 90, 80, 40, 50]
for x in my_scores:
    sum += x
print('test1', sum)
print('test2', sum / len(my_scores))
print('test3', statistics.mean(my_scores))

class_scores = [[30, 90, 80, 40, 50],
                [100, 100, 100, 100, 100],
                [90, 90, 30, 30, 20]]

sum = 0
for x in range(0, 3):
    for y in range(0, 5):
        print(class_scores[x][y])
        sum += class_scores[x][y]
print(sum / 15)
print(sum / (len(class_scores[0]) + len(class_scores[1]) + len(class_scores[2])))

sum_t = 0
avg_t = 0
num = 0


# for x in class_scores:
#    sum_t += sum(x)
#    num += len(x)
#
# avg_t = sum_t/num


def double(n):
    return n * 2


print(double(1))
print(double(2))


def add(x, y):
    return x + y


print(add(1, 3))

for i in range(2, 9 + 1):
    for j in range(1, 9 + 1):
        print(i, '*', j, '=', i * j)

for j in range(1, 10):
    i = 3
    print(i, '*', j, '=', i * j)
# 1. total 함수 만들기
# 2. average 함수 만들기
# 3. 제대로 했는지 확인하기
# 4. github에 올리기
scores = [80, 100, 70, 90, 40]


def total(scores):
    sum = 0
    for x in scores:
        sum += x
    return sum


print(total(scores))


def average(scores):
    sum = 0
    for x in scores:
        sum += x
    return sum / len(scores)


print(average(scores))
