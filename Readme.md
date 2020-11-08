# NumRoll

## Objective
	The NumRoll project is essentially a handwritten number recognition system with a UI interface including canvases, buttons, and triggered reactions that ultimately secure the user's files such as homework. Instead of the traditonal code-access system, NumRoll adds a special twist by prompting users to handwrite their passcode. To execute NumRoll, the users will be using the terminal command lines. This document is written based on the Linux command lines (Ubuntu).

## Install Dependencies
1. open up a terminal window on your device by using Keyboard shortcut or from launchpad
2. Copy the link from NumRoll's master branch
3. Go to the directory where you would like to run the program, enter in the terminal "git clone <link>" (repleace <link> with the link you have copied)
4. If git is not installed on your device, simply install it from the package manager. For example, "sudo apt-get git" on Ubuntu or "sudo pacman -S git" on Arch-Linux
5. cd into the NumRoll folder, then install all the dependencies using pip3: "pip3 install -r requirements.txt"
6. If pip is not installed, simply use package manager to install it
7. Install VLC media player using the package manager if not pre-installed

## Run the program
In the same terminal window, run "python3 main.py", the GUI should pop up and you can follow the instructions. When you enter the correct code, the homework page should show up as a .txt file. Try different combinations to unlock the bonus ending!

### Customize your own passcode to unlock
1. Make sure some kind of text editor such as vim or atom is installed in your system. Open up main.py using your text editor
2. Find the line of code "conpare('12345')" under function "def start_pushed()", change the 5-digit string to any 5-digit numeral code you would like to use. 
3. Write into the code by pressing the escape key first, then enter ":wq" to write and quit.
4. Now test the new passcode by running main.py.


