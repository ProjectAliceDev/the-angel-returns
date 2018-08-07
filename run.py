#!usr/bin/env python
import os


# Set this variable equal to the location of where your Ren'Py install is!
sdk_location = "/Applications/RenPy\ SDK\ \(DDLC-compatible\)/renpy.sh"


def show_version_copyright():
    print("Angle Alice Script Test Tool")
    print("(C) 2018 | Project Alice.")
    print("Licensed under GNU GPL v3.")


def print_error():
    print("We couldn't test your changes to the code.")
    print("This likely means that your build will not function properly during auto-builds.")


def create_dummy_version():
    try:
        print("Creating a dummy version file...")
        with open('version', 'w+') as fd:
            fd.write("{\"version\":\"dummy\"}")
        print("Version file created.")
        return 0
    except Exception as e:
        print("Something went wrong when creating the version file.")
        print("You can search for the error here: " + str(e))
        return 1


def run_renpy():
    try:
        print("Attempting to run the mod in the Ren'Py SDK...")
        os.system(sdk_location + " .")
        return 0
    except Exception as e:
        print("Something went wrong when trying to run Ren'Py.")
        print("You can search for the error here: " + str(e))
        return 1


def delete_dummy_version():
    print("Deleting dummy version file...")
    try:
        os.remove('version')
        return 0
    except Exception as e:
        print("Something went wrong when trying to delete the version file.")
        print("You can search for the error here: " + str(e))
        return 1


if __name__ == "__main__":
    show_version_copyright()
    version_check = create_dummy_version()
    if version_check != 0:
        print_error()
    else:
        pass

    launcher_check = run_renpy()
    if launcher_check != 0:
        print_error()
    else:
        pass

    delete_check = delete_dummy_version()
    if delete_check != 0:
        print_error()
    else:
        pass

    if version_check == 0 and launcher_check == 0 and delete_check == 0:
        print("Success!")
        print("Don't forget to commit your changes to GitHub.")
