import os
import sys

dir = os.path.dirname(__file__) + '/img'

for f in os.listdir(dir+'/coins'):
    print(f + ': ' + str(os.path.isfile(dir + '/' + f)))

# print(dir)
