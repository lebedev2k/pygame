import os

# imgRight = [
#     ('platformer/img/hero/2_enemies_1_walk_000.png', 100),
#     ('platformer/img/hero/2_enemies_1_walk_001.png', 100),
#     ('platformer/img/hero/2_enemies_1_walk_002.png', 100),
# ]


def getPygAnimListFromDir(folder, delay):
    res = []
    a = os.listdir(folder)
    for i in a:
        s = folder + '/' + i
        if os.path.isfile(s):
            res.append((s, delay))
    return res


# a = getPygAnimList('platformer/img/coins/1', 100)
# print(a)
