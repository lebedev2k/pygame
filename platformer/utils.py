import os


def getPygAnimListFromDir(dirpath, delay):
    res = []

    for a in os.listdir(dirpath):
        s = dirpath+'/'+a
        if os.path.isfile(s):
            res.append((s, delay))
        # print(s)

    return res


# path = os.path.dirname(__file__)+'/img/coins/1'
# animList = getPygAnimListFromDir(path, 100)
# print(animList)
