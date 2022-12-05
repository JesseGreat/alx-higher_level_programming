if __name__ == "__main__":
    from sys import argv

    argv_no = len(argv)
    n = argv_no - 1
    result = 0
    if argv_no == 1:
        print(f"{n}")
    elif argv_no == 2:
        print(f"{argv[n]}")
    elif argv_no >= 3:
        for i in range(1, argv_no):
            numb = int(argv[i])
            result += numb
        print(f"{result}")
