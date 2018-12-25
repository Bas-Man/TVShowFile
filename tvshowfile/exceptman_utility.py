import exceptman


def setup():
    global ExMan
    ExMan = exceptman.ExceptionListManager()
    ExMan.loadExceptionList()
    return ExMan.exportList()


def print_dict(d):
    for k, v in d.items():
        if isinstance(v, dict):
            print("Main Key: {}".format(k))
            print_dict(v)
        else:
            print("\t{0} : {1}".format(k, v))


def main():
    ExceptList = setup()
    print_dict(ExceptList)
    print("Key: s.w.a.t")
    print_dict(ExceptList['s.w.a.t'])


if __name__ == '__main__':
    main()
