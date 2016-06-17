# README #

I made this while I was learning how to program, so this code is about 95% garbage. I would recommend staying away from it. 
I have a better version written in C# that I'll put up soon.

### Escapists Map Tools ###

This is a tool I quickly whipped up for personal use that can

* Enable editing of a map by decrypting it, setting Info.Custom to -1 and Info.Rdy to 0 and re-encrypting it with a given encryption key
* Decrypt a map with a given encryption key
* Encrypt a map with a given encryption key

The Escapists uses blowfish-compat as the encryption, and the default key is mothking.

### Dependencies ###

* PyCrypto
* [blowfish-compat.py](https://gist.github.com/adamb70/1f140573b37939e78eb5) Made by adamb70 (Rename it to blowfish_compat.py)
* (OPTIONAL) argparse - Only if you would like to use commandline arguments.
