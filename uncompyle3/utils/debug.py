f = open("/home/dfx/src/uncompyle3/debug.log", "w")
f.close()

def debug(*data):
    line = " ".join(str(i) for i in data) + "\n"
    f = open("/home/dfx/src/uncompyle3/debug.log", "a")
    f.write(line)
    f.close()
    #print(line)
