f = open('/home/dfx/src/decompilers/uncompyle3/uncompyle3/debug.log', 'w')
f.close()

def debug(*data):
    line = ' '.join(str(i) for i in data) + '\n'
    f = open('/home/dfx/src/decompilers/uncompyle3/uncompyle3/debug.log', 'a')
    f.write(line)
    f.close()
    #print(line)
