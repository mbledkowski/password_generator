# Password generator by @mmble
Password generator written in Python
## Screenshots:
#### Command Line Interface version:
![CLI screenshot](https://github.com/mmble/password_generator/blob/master/screenshotcli.jpg)
#### Graphical User Interface version:
![GUI screenshot](https://github.com/mmble/password_generator/blob/master/screenshotgui.jpg)
## Commands for generating executables:
#### Command Line Interface version:
```bash
cd "./Command Line Interface Version"
```
```bash
pyinstaller --noconfirm --onefile --console --icon "./icon.ico" --name "Password generator CLI" --ascii  "./main.py"
```
#### Graphical User Interface version:
```bash
cd "./Graphical User Interface Version"
```
```bash
pyinstaller --noconfirm --onefile --windowed --icon "./icon.ico" --name "Password generator GUI" --ascii --add-data "./icon.ico;."  "./main-pyinstaller_version.py"
```
## Technologies:
 - Python 
   - "random" and "string" build-in libraries
 - TkInter (in GUI version)
 - pyinstaller (and its GUI overlay - auto-py-to-exe)
