# JunkRat
JunkRat is a classic 2D platforming game with a twist. The JunkRat flies using a jetpack and is controlled with the WASD keys. The goal is to reach the flag to proceed to the next level. Beat all 5 levels and you win!

## Getting Started
---
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.

python3 -m pip install raylib

After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.```

python3 junkrat

You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure
---
The project files and folders are organized as follows:

root                    (project root folder)
+-- junkrat             (source code for game)
  +-- game              (specific game classes)
    +-- casting         (various actor classes)
    +-- directing       (director and scene manager classes)
    +-- scripting       (various action classes)
    +-- services        (various service classes)
  +-- __main__.py       (entry point for program)
  +-- constants.py      (game constants)
+-- README.md           (general info)


## Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7

## Author
---
* Erik Rutledge
* CSE 210 Student
* BYUI Fall Sememster 2022