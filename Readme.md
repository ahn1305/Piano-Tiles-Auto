# Automating Piano Tiles Game using python

<img src = "Images/main.jpg" height= "300" />


The idea of the project is to automate the piano tiles game that can work on any screen resolution and <br />
if the game is running on the specific website that is mentioned here.
<br /><br />
(Note): This project only runs on windows since we are using win32api (available only for windows).

## Instructions to setup the project

1. Clone the project:
open cmd as administrator and type in the following command <br /> 
(or) <br />
download the zip and extract it:

```
git clone https://github.com/ahn1305/Piano-Tiles-Auto.git
```
2. Install the required packages
Install these libraries from an administrator terminal:
```
pip install pywin32
pip install keyboard
pip install pyautogui
pip install opencv-python
```
3. Go to https://www.agame.com/game/magic-piano-tiles and click on play button.

4. Then open cmd inside the project and run the Bot.py file:
```
python .\Bot.py
```
&nbsp;&nbsp;&nbsp;&nbsp;Now there will be a 20 sec gap for the program to run, during this time follow the 5th step

5. Go the website you opened and click on ``` f11 ``` button to enter fullscreen <br />
then press on the following button shown in the image below

<img src = "Images/fullscrnbtn.png" height= "400" width="600" /> <br />

Now your screen should be looking something like this:

<img src = "Images/fs.jpg" height= "500" width="700" /> <br />

<hr />

And that's it, Now click on the start button to see the magic !!
