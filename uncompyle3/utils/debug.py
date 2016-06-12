import os
import sys


def get_log_path():
    path = os.path.dirname(os.path.realpath(os.path.abspath(sys.argv[0])))
    path = os.path.join(path, 'debug.log')
    return path

f = open(get_log_path(), 'w')
f.close()



def debug(*data):
    line = ' '.join(str(i) for i in data) + '\n'
    f = open(get_log_path(), 'a')
    f.write(line)
    f.close()
    #print(line)
