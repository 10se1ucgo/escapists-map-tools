import sys

import maptools

try:
    import easygui

    easygui_enabled = True
except ImportError:
    easygui_enabled = False

try:
    import argparse

    argparse_enabled = True
except ImportError:
    argparse_enabled = False


def main():
    if argparse_enabled:
        commandln()
    elif easygui_enabled:
        print "argparse not found, using GUI instead"
        gui()
    else:
        print "Neither argparse nor easygui was found, cannot continue. Please install one of the two."
        sys.exit()


def commandln():
    parser = argparse.ArgumentParser(description='Escapists Map Tools')
    parsegroup = parser.add_mutually_exclusive_group()
    parsegroup.add_argument("-dc", "--decompile", type=str, nargs=2, metavar=('map_file.map', 'encryption_key'),
                            help="Decompiles a map with a given encryption key")
    parsegroup.add_argument("-d", "--decrypt", type=str, nargs=2, metavar=('map_file.map', 'encryption_key'),
                            help="Decrypts a map with a given encryption key")
    parsegroup.add_argument("-e", "--encrypt", type=str, nargs=2, metavar=('map_file.map', 'encryption_key'),
                            help="Encrypts a map with a given encryption key")
    args = parser.parse_args()

    if args.decompile != None:
        maptools.decompilemap(args.decompile[0], args.decompile[1])
    elif args.decrypt != None:
        maptools.decryptmap(args.decrypt[0], args.decrypt[1])
    elif args.encrypt != None:
        maptools.encryptmap(args.encrypt[0], args.encrypt[1])
    elif easygui_enabled == False:
        print "Module easygui not installed. Only the command-line interface is available."
        parser.print_usage()
    else:
        print "No command line arguments, using GUI."
        gui()


def gui():
    option = easygui.buttonbox("Select an option.", "Escapists Map Tools",
                               ["Decompile a map", "Decrypt a map", "Encrypt a map"])
    if option == "Decompile a map":
        key = easygui.enterbox("Enter encryption key (Default: mothking)", option, "mothking")
        maptools.decompilemap(easygui.fileopenbox(), key)
    elif option == "Decrypt a map":
        key = easygui.enterbox("Enter encryption key (Default: mothking)", option, "mothking")
        maptools.decryptmap(easygui.fileopenbox(), key)
    elif option == "Encrypt a map":
        key = easygui.enterbox("Enter encryption key (Default: mothking)", option, "mothking")
        maptools.encryptmap(easygui.fileopenbox(), key)


if __name__ == '__main__':
    main()
