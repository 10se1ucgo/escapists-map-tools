import os.path

import configparser

import blowfish_compat


def decompilemap(file_path, encryption_key):
    temp_file = file_path + ".tmp"
    final_file = os.path.splitext(file_path)[0] + ".proj"
    print "Decrypting with the key %s." % encryption_key
    blowfish_compat.decrypt(file_path, temp_file, encryption_key)
    print "Done."
    properties = configparser.ConfigParser(allow_no_value=True)
    properties.read(temp_file)
    print "Parsing decrypted map file"
    if not properties.has_option("Info", "Rdy") or not properties.has_option("Info", "Custom"):
        print "Map missing Rdy and/or Custom flags, adding..."
        properties.set("Info", "Rdy", "0")
        properties.set("Info", "Custom", "-1")
        print "Done."
    else:
        print "Setting Info.Rdy to 0 and Info.Custom to -1..."
        properties.set("Info", "Rdy", "0")
        properties.set("Info", "Custom", "-1")
        print "Done."
    with open(temp_file, "w") as mapfile:
        properties.write(mapfile)
    print "Written to %s." % temp_file
    os.remove(temp_file)
    print "Temp file removed"
    print "Complete"


def decryptmap(file_path, encryption_key):
    final_file = os.path.splitext(file_path)[0] + ".decrypted.map"
    print "Decrypting with the key %s" % encryption_key
    blowfish_compat.decrypt(file_path, final_file, encryption_key)
    print "Done"


def encryptmap(file_path, encryption_key):
    final_file = os.path.splitext(file_path)[0] + ".encrypted.map"
    print "Encrypting with the key %s" % encryption_key
    blowfish_compat.encrypt(file_path, final_file, encryption_key)
    print "Done"
