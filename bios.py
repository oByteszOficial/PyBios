import OS

def main():
    bSelect = input("press B to enter bios")
    if bSelect == "b":
        bios()
    elif bSelect == "B":
        bios()
    else:
        print(" \n \n \n \n \n \n \n \n \n \n \n ")
        OS.load()

def bios():
    print("entering setup...")
    SIM(5, "quit", "date and time settings", "boot order", "save settings", "restore default")
    opt = input(": ")

def SIM(opqt, op1, op2, op3, op4, op5):
    print(" \n \n \n \n \n \n \n \n \n \n \n \n ")
    if opqt == 1:
        print("|")
        print("| 1. ", op1, "|")
        print("|")
    elif opqt == 2:
        print("|")
        print("| 1. ", op1, ";")
        print("| 2. ", op2, ";")
        print("|")
    elif opqt == 3:
        print("|")
        print("| 1. ", op1, ";")
        print("| 2. ", op2, ";")
        print("| 3. ", op3, ";")
        print("|")
    elif opqt == 4:
        print("|")
        print("| 1. ", op1, ";")
        print("| 2. ", op2, ";")
        print("| 3. ", op3, ";")
        print("| 4. ", op4, ";")
        print("|")
    elif opqt == 5:
        print("|")
        print("| 1. ", op1, ";")
        print("| 2. ", op2, ";")
        print("| 3. ", op3, ";")
        print("| 4. ", op4, ";")
        print("| 5. ", op5, ";")
        print("|")
    else:
        print("error on 'bios.SIM(qt)'")
        print("                   --")
        print("                    here")
        print("invalid value, the max value it's 5.")

print("BIOS WhiteLabel VM")
print("selected os: PythonBase")
main()