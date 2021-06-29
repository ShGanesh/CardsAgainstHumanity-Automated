## [play_v1.py](play_v1.py)   
1. Ask for a number between 1 to 10, and print *blackCard* statement.   
2. Directly add random *whiteCard* phrases into the *blackCard* statement.  
3. Output the result  
4. End  

## [play_v2.py](play_v2.py)
1. Show a brief description of the game  
2. Ask if you want to save the output  
    1. (y | Y): All subsequent outputs will be appended to a file called **CAH_OP.txt** (If it doesn't exist it will be created automatically).  
    2. (n | N): Outputs will only be outputted in the terminal/Command_Line     
    3. !(y|n|Y|N): Loop back to point 2
3.  Start Game {nth iteration of game}
4.  Ask for a number between 1 to 10, and print *blackCard* statement.  
5.  Directly add random *whiteCard* phrases into the *blackCard* statement.  
6.  Output the result
7.  Ask if player wants to continue the game
    1. (y | Y): Loop back to poiint 3
    2. !(y | Y): End  

## [play_v3.py](play_v3.py)
1. Show a brief description of the game  
2. Ask if you want to save the output  
    1. (y | Y): All subsequent outputs will be appended to a file called **CAH_OP.txt** (If it doesn't exist it will be created automatically).  
    2. (n | N): Outputs will only be outputted in the terminal/Command_Line     
    3. !(y|n|Y|N): Loop back to point 2
3.  Start Game {nth iteration of game}
4.  Ask for a number between 1 to 10, and print *blackCard* statement.  
    1. If input is a number: continue
    2. If input == "exit": exit. Thanks message sent. 
6.  Directly add random *whiteCard* phrases into the *blackCard* statement.  
7.  Output the result
8.  Loop back to point 3

## [play_v4.py](play_v4.py)  
1. Show a brief description of the game (improved)  
2. Ask if you want to save the output  
    1. (y | Y): All subsequent outputs will be appended to a file called **CAH_OP.txt** (If it doesn't exist it will be created automatically).  
    2. (n | N): Outputs will only be outputted in the terminal/Command_Line     
    3. !(y|n|Y|N): Loop back to point 2
3.  Start Game {nth iteration of game}
4.  Ask for a number between 1 to 10, and print *blackCard* statement.  
    1. If input is a number: continue
    2. Wait for 1 sec  
    3. If input == "exit": exit. Thanks message sent. 
6.  Wait for 0.5 sec  
7.  Directly add random *whiteCard* phrases into the *blackCard* statement.  
8.  Wait for 2 sec  
9.  Output the result
10.  Loop back to point 3
