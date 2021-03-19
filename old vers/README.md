# thousand_dice_simulator
Simulates 1000s of dice rolls and outputs statistical analysis in less than a second.

Records each randomly generated number into a CSV file.
Statistical analysis and simulation speed is provided in terminal/powershell or in the CSV.

How to Use: 

1. Make sure you have python installed on your mac or PC: Google "how tell if python installed on PC." Most Macs and Linux OSes will have it installed already.
2. Download dice_roll_sim.py. Note the directory to which it is downloaded. (usually "downloads")
3. Run dice_roll_sim.py. To do this, do the following: 
 a. On Windows: 1) Open the command prompt. 
 b. In command prompt, go to directory. In most cases, you should be able to type in "cd downloads", going straight to the "downloads" working directory. 
 c. From here, type: "py dice_roll_sim.py." 
 d. If successful, it should provide statistical analysis and simulation speed in the same window. You can also find the newly generated CSV file in the same folder as the .py file. Use a text editor or Excell to open and read it. 
#note: Instructions for Mac and Linux OS TBA (but are quite simular). 
Alternatively, if you have a programming IDE installed, like PyCharm or VisualStudio, you can easily run the code in them.

To change the number of simulations / type of dice rolled:
1. Open dice_roll_sim.py in a text editor.
2. Close to the top, change the values of sim_count (the number of simulations) and dice_size.
3. Warning: Changing anything can result in difficult to fix bugs. Uber-large numbers can slow any computer down. If the computer gets stuck, press Control + C to end the current process, 

Currently, 1000 dice rolls are simulated in .27 seconds.
NOTE: Future versions, if there are any, will focus on ease-of-use: for use of the command-line prompt and GUIs. 
