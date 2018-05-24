import os

default = os.path.dirname(os.path.abspath(__file__))
gamedir = os.path.join(default, "game")
chardir = os.path.join(default, "characters")
allo = os.path.join(default, "/game/ddtar.rpa")

print("Remember: this script works ONLY in Python 3!")
checkuninstall = input("Are you sure you want to uninstall Doki Doki: The Angel Returns? (Yes/No):")

if checkuninstall == "Yes":
    try:
        os.remove(default + "/characters/aliceangel.chr")
        os.remove(default + "/game/ddtar.rpa")
        filelist = [ f for f in os.listdir(gamedir) if f.endswith(".rpyc") ]
        for f in filelist:
        	os.remove(os.path.join(gamedir, f))
        print("All files deleted successfully.")
    except:
        print("Whoops, something went wrong...")
else:
    print("Abort.")
