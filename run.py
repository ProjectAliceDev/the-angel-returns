import os

# Set this variable equal to the location of where your Ren'Py install is!
renpy = "/Applications/RenPy\ SDK\ \(DDLC-compatible\)/renpy.sh"

print("Running DDTAR in developer mode...")

try:
    os.system(renpy + " .")
except:
    print("Whoops, something went wrong.")
    print("Check your RENPY variable in run.py.")
