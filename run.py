import sys
import Tkinter
import tkFileDialog

import maptools

try:
    import _winreg as winreg

    winmachine = True
except ImportError:
    winmachine = False

try:
    import argparse

    argparse_enabled = True
except ImportError:
    argparse_enabled = False


def main():
    if argparse_enabled:
        commandln()
    else:
        print "argparse not found, using GUI instead"
        gui()


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
    else:
        print "No command line arguments, using GUI."
        gui()


class maptoolsgui:
    def __init__(self, winname):
        self.winname = winname
        winname.title("Escapists Map Tools")

        self.label = Tkinter.Label(winname, text="Select an action")
        self.label.pack(side="top")

        self.decompmap = Tkinter.Button(winname, text="Decompile a map", command=lambda: self.enterkey(1))
        self.decompmap.pack(side="left")

        self.dcryptmap = Tkinter.Button(winname, text="Decrypt a map", command=lambda: self.enterkey(2))
        self.dcryptmap.pack(side="left")

        self.ecryptmap = Tkinter.Button(winname, text="Encrypt a map", command=lambda: self.enterkey(3))
        self.ecryptmap.pack(side="left")

    def enterkey(self, somevariable):

        if somevariable == 1:
            self.action = 1
        elif somevariable == 2:
            self.action = 2
        elif somevariable == 3:
            self.action = 3

        self.keylevel = Tkinter.Toplevel()
        self.keylevel.title("Enter encryption key")
        self.keylevel.protocol("WM_DELETE_WINDOW", self.winname.destroy)
        self.keylevel.focus_set()
        self.winname.withdraw()

        self.label = Tkinter.Label(self.keylevel, text="Enter an encryption key (Default: mothking)")
        self.label.pack()

        self.entry = Tkinter.Entry(self.keylevel)
        self.entry.pack()
        self.entry.insert(0, "mothking")

        self.okay = Tkinter.Button(self.keylevel, text="OK", command=self.dotheactionyo)
        self.okay.pack(side="left")

        self.cancel = Tkinter.Button(self.keylevel, text="Cancel", command=sys.exit)
        self.cancel.pack(side="right")

    def dotheactionyo(self):

        self.encryptkey = self.entry.get()
        self.keylevel.destroy()
        self.filepath = tkFileDialog.askopenfilename(defaultextension=".map",
                                                     filetypes=[('Escapists map file', '*.map'),
                                                                ('Escapists project file', '*.proj'),
                                                                ('All files', '*.*')],
                                                     initialdir=self.escapistspath())
        if not self.filepath:
            sys.exit()
        elif self.action == 1:
            maptools.decompilemap(self.filepath, self.encryptkey)
        elif self.action == 2:
            maptools.decryptmap(self.filepath, self.encryptkey)
        elif self.action == 3:
            maptools.encryptmap(self.filepath, self.encryptkey)

    def escapistspath(self):

        if winmachine:
            try:
                self.steam_reg_path = r"Software\Valve\Steam"
                self.reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.steam_reg_path, 0, winreg.KEY_READ)
                self.value, regtype = winreg.QueryValueEx(self.reg_key, r"SteamPath")
                return self.value + r"/steamapps/common/The Escapists/Data/Maps"
            except WindowsError:
                return None
        else:
            return None


def gui():
    window = Tkinter.Tk()
    maptoolsgui(window)
    window.mainloop()


if __name__ == '__main__':
    main()
