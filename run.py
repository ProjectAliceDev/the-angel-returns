#!usr/bin/env python

import os

# Set this variable equal to the location of where your Ren'Py install is!
renpy = "/Applications/RenPy\ SDK\ \(DDLC-compatible\)/renpy.sh"

try:
    # Run DDTAR via RenPy
    os.system(renpy + " .")
except:
    print("Whoops, something went wrong.")
    print("Check your RENPY variable in run.py.")
