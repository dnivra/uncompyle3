#!/usr/bin/env python3

if __name__ == "__main__":


    import argparse

    from uncompyle3.uncompyle import Uncompyle


    argparser = argparse.ArgumentParser(description="Bytecode decompiler for CPython 3.x")
    argparser.add_argument("file", help="path to file with bytecode")
    args = argparser.parse_args()

    file = open(args.file, "rb")
    file_bytes = file.read()
    file.close()

    uncompyle = Uncompyle()


    print(uncompyle.run(file_bytes))
