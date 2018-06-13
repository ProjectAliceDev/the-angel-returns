# Developer Notes

> To view any new functions or changes made to extend DDLC, please see [CHANGES.md](CHANGES.md).

## Developing for Yourself (Non-contribution)
If you plan to make your own project from this one, please fork this to your account and follow the guidelines listed in IPGuidelines.md before continuing.


## Contributing to the Mod
If you are a collaborator on this project, it is recommended that you work in a separate branch before continuing. Branches can be sorted by either milestone or by user.

Most developer sessions that happen in real-time should make use of the  `sanctuary` Discord channel for communications and seamless integration.

**Any changes should be reviewed in a pull request before being committed to the master branch.**

> Note: Please make sure your code follows the style guidelines (to be written soon).

### Recommended Tools
* Atom
* Ren'Py SDK
* Python

> Note: It is not absolutely required for you to use Atom to contribute to the project. Please use the editor of your choice.

#### Using Atom? Install these plugins
* `teletype` - allows real-time collaboration features
* `renpy` - adds official Ren'Py language support
* `tool-bar` - adds a toolbar to Atom
  * `flex-tool-bar` - adds additional buttons to toolbar
* `script` - allows running of scripts from Atom directly

### Using `run.py` to test changes
At the root directory, `run.py` exists as a quick method of launching the game and testing any changes you have made. This can prove useful and can conserve taskbar/dock space if you do not want to keep the Ren'Py Launcher open. At the time of writing, this script only works on macOS/Linux as it requires a UNIX shell to execute. Changes to the script that include Windows support is highly welcomed.

To allow `run.py` to work properly on your system, change the string in the variable declaration of `renpy` to where your `renpy.sh` is located (should be at the root of the Ren'Py SDK folder.)

#### Running the script in Atom
To test any new changes or to run the game in a debug state, open the `run.py` file in Atom and click the Play button ("Run Python Project"). 

#### Running the script in Python
Alternatively, you can run the command `python3 run.py` into the Terminal.