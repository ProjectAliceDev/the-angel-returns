# Development of DD:TAR

## Required Tools
* Atom
* Ren'Py SDK
* Python
* A GitHub account

## Required Atom Plugins
* `teletype` - allows collaboration features
* `renpy` - adds official Ren'Py language support
* `tool-bar` - adds a toolbar to Atom
  * `flex-tool-bar` - adds additional buttons to toolbar
* `script` - allows running of scripts from Atom directly

## Testing Changes
To test any new changes or to run the game in a debug state, open yp the `run.py` file in Atom and click the Play button ("Run Python Project"). Alternatively, you can make a symbolic link to your Ren'Py projects folder and launch the game through the Ren'Py Launcher.

> Note: You _must_ change the variable set in `run.py` to your location of `renpy.sh` so that it works correctly!

## Contributing to the Mod
If you are a collaborator on this project, it is recommended that you work in a separate branch before continuing.

Most developer sessions that happen in real-time should make use of the `teletype` package in addition to the `sanctuary` Discord channel for communications and seamless integration.

Any changes should be reviewed in a pull request before being committed to the master branch.

> Note: Please make sure your code follows the style guidelines (to be written soon).

## Developing for Yourself (Non-contribution)
If you plan to make your own project from this one, please fork this to your account and follow the guidelines listed in IPGuidelines.md before continuing.
