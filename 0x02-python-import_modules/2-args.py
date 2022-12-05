#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    argv_no = len(argv)
    n = argv_no - 1
    if argv_no == 1:
        print(f"{n} arguments.")
    elif argv_no == 2:
        print(f"{n} argument:")
        print(f"{n}: {argv[n]}")
    elif argv_no >= 3:
        print(f"{n} arguments:")
        for i in range(1, argv_no):
            print(f"{i}: {argv[i]}") 
