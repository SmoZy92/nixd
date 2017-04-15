import crypt
from termcolor import colored


def testPass(cryptPass):
    salt = cryptPass[0:2]
    cracklist = open("rockyou.txt", "r")
    for word in cracklist.readlines():
        word = word.strip("\n")
        cryptWord = crypt.crypt(word, salt)
        if (cryptWord == cryptPass):
            print colored("[+] Password Found : %s \n" % word, "green")
            return
    print colored("[-] Password Not Found. \n", "red")
    return


def main():
    f = open("passwords.txt")
    for line in f.readlines():
        if ":" in line:
            user = line.split(":")[0]
            cryptPass = line.split(":")[1].strip(" ")
            print colored("[*] Cracking password for: %s" % user, "cyan")
            testPass(cryptPass)


if __name__ == "__main__":
    main()
