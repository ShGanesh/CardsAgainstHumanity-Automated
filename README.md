# CardsAgainstHumanity-Automated (basic) 
An Automated (and slightly modified) version of Cards Against Humanity.  
Latest Version: [play_v4.py](main/play_v4.py).

## Main  
Main game is supposed to contain two text files (blackCards.txt and whiteCards.txt) and a main .py file ([play_v1.py](main/play_v1.py), [play_v2.py](main/play_v2.py),  [play_v3.py](main/play_v3.py) and [play_v4.py](main/play_v4.py).  
- Text file [blackCards.txt](main/blackCards.txt) contains questions which initiate an instance of a CAH game.
- Text file [whiteCards.txt](main/whiteCards.txt) contains ... weird phrases which can be added to questions from the blackCards.txt 

To Start the Game, the Player (**Card Czar**) shall draw one card out of the 10 randomized black cards provided by the script.  
The script shall randomly select phrases from whiteCards.txt and attach them to the provided Question. The **Card Czar** has to read the output statement out loud.
The person who loses their sh\*t first shall become the new **Card Czar** and continue the cycle.  
If the current **Card Czar** fails to make anyone laugh they shall start acting like a sentient monkey and then initiate another instance of the game.  
Additional failiures shall lead to the **Card Czar** accepting different genera, which shall be left to the descretion of other players.

## Installation  
Download the latest .py file and the two .txt files (present in the main folder) and move them into the same directory/folder.  
Run the .py file.
