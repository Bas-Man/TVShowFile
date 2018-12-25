import exceptman
import sys


def setup():
    global ExMan
    ExMan = exceptman.ExceptionListManager()
    ExMan.loadExceptionList()


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
    print("\tq to quit")
    print("\tlist to list all keys and values")
    print("\tkey list values for given key")
    print("\tadd to add a new key and values")
    print("\th to list these commands")
    print("")


def addKey(d):
    newKey = input("Enter new key:  ")
    keepPeriods = input("keepPeriods t or f:  ")
    name = input("Show Name as you would like it to appear or leave blank:  ")

    if d.hasKey(newKey):
        print("Key: {} exists. Nothing done.".format(newKey))
    else:
        d.ExceptList[newKey] = {}
        if keepPeriods == 't':
            d.ExceptList[newKey]['keepPeriods'] = True
        else:
            d.ExceptList[newKey]['keepPeriods'] = False
        if name != '':
            d.ExceptList[newKey]['name'] = name
        d._updated = True


def main():
    run = True
    setup()
    list_commands()
    while run:
        command = input("Enter Command:  ")
        if command == 'q':
            run = False
            if ExMan._updated:
                dosave = input("Do you want to save your changes?  ")
                if dosave == 'y':
                    print("Saving")
                else:
                    print("Changes not saved")
            sys.exit()
            break
        elif command == "list":
            print_dict(ExMan.ExceptList)

        elif command == "key":
            subcommand = input("Enter key: ")
            print_by_key(ExMan, subcommand)

        elif command == "h":
            list_commands()

        elif command == "add":
            addKey(ExMan)

if __name__ == '__main__':
    main()
