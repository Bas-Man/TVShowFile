import exceptman
import sys


def setup():
    global ExMan
    ExMan = exceptman.ExceptionListManager()
    ExMan.loadExceptionList()
    # return ExMan.exportList()


def print_dict(d):
    for k, v in d.items():
        if isinstance(v, dict):
            print("Main Key: {}".format(k))
            print_dict(v)
        else:
            print("\t{0} : {1}".format(k, v))


def print_by_key(d, key):
    if d.hasKey(key):
        print("Key: {}".format(key))
        print("Name: {}".format(d.ExceptList[key].get('name')))
        print("KeepPeriods is {}".format(
            d.ExceptList[key].get('keepPeriods', 'false')))
    else:
        print("There is no key: {}".format(key))


def list_commands():
    print("Commands List:")
    print("\tQ/q to quit")
    print("\tlist to list all keys and values")
    print("\tkey list values for given key")
    print("\th to list these commands")
    print("")


def main():
    run = True
    setup()
    list_commands()
    while run:
        command = input("Enter Command: ")
        if command == 'q':
            run = False
            sys.exit()
            break
        elif command == "list":
            print_dict(ExMan.ExceptList)

        elif command == "key":
            subcommand = input("Enter key: ")
            print_by_key(ExMan, subcommand)

        elif command == "h":
            list_commands()


if __name__ == '__main__':
    main()
