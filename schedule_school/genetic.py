import numpy as np
from collections import defaultdict


NUM_OF_TEACHERS = 10
NUM_OF_CLASSES = 10
NUM_OF_LESSONS = 20
weighted_lessons = (geom, alg, lang, chem, phys, bio, ukr_lang,
                    urk_lit, hist) = range(9)
weights = (6, 5.5, 5.4, 5.3, 5.2, 3.6, 3.5, 1.7, 1.7)
weights = defaultdict(lambda: 1)
for lesson, w in zip(weighted_lessons, w):
    weights[lesson] = w

LOW = 2
HIGHT = 8


def random_day():
    return [[np.random.randint(i) for i in [NUM_OF_TEACHERS, NUM_OF_CLASSES,
                                         NUM_OF_LESSONS]]
            for _ in range(np.random.randint(LOW, HIGHT))]


def random_class_schedule():
    return [random_day() for _ in range(7)]


def random_schedule():
    return [random_class_schedule() for _ in range(NUM_OF_CLASSES)]


def overlap(schedule):
    days1 = set()
    days2 = set()
    for class_schedule in schedule:
        for day_num, day_schedule in enumerate(class_schedule):
            for lesson_pos, (teacher, class_, _) in enumerate(day_schedule):
                if ((day_num, lesson_pos, teacher) in days1
                    or (day_num, lesson_pos, class_) in days2):
                    return True
                days1.add((day_num, lesson_pos, teacher))
                days2.add((day_num, lesson_pos, class_))
    return False


def fit_hours(schedule):
    teachers = defaultdict(int)
    for class_schedule in schedule:
        for day_num, day_schedule in enumerate(class_schedule):
            for (teacher, _, _) in day_schedule:
                teachers[teacher, day_num] += 1
    for hours in teachers.values():
        if hours > 27:
            return 0
    return 1


def fitness(schedule):
    if overlap(schedule):
        return 0
    else:
        fits = [fit_hours, fit_complexity]
        estimations = [est(schedule) for est in fits]
        return np.exp(np.sum(estimations))


rs = random_schedule()
finished = fitness(rs)
print(fit_hours(rs))
