import controllers.Time as time


def t(hour=0, minute=0):
    return time.CreateTime(hour, minute)


schemes = {
    1: {
        1: [t(8, 50), t(9, 35)],
        2: [t(9, 40), t(10, 25)],
        3: [t(10, 40), t(11, 25)],
        4: [t(11, 30), t(12, 15)],
        5: [t(12, 50), t(13, 30)],
        6: [t(13, 30), t(14, 10)],
        7: [t(14, 25), t(15, 5)],
        8: [t(15, 10), t(15, 55)]
    },
    2: {
        1: [t(8, 50), t(9, 35)],
        2: [t(9, 40), t(10, 25)],
        3: [t(10, 40), t(11, 25)],
        4: [t(11, 30), t(12, 15)],
        5: [t(12, 50), t(13, 30)],
        6: [t(13, 30), t(14, 10)]
    },
}

day_scheme = [schemes[1], schemes[1], schemes[2], schemes[1], schemes[1]]
