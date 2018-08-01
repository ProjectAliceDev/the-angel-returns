import os

# Set this variable equal to the location of where your Ren'Py install is!
renpy = "/Applications/RenPy\ SDK\ \(DDLC-compatible\)/renpy.sh"

try:
    # Compile all RPYCs first. This way. GOBFADU works properly.
#    os.system(renpy + " . compile")

    # Run DDTAR via RenPy
    os.system(renpy + " .")
    
    # Finally, clean up the data by removing all of the RPYCs and DS_Store files
    # which are usually dropped by Mac OS X.
    os.system("find . -type f -iname \*.DS_Store -delete")
#    os.system("find . -type f -iname \*.rpyc -delete")
except:
    print("Whoops, something went wrong.")
    print("Check your RENPY variable in run.py.")
