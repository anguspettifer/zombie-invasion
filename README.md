# zombie-invasion

## How to use this repo

- Clone the repo and install requirements into a virutal environment <br>
- Run <code>python play_game </code> <br>
- Follow the instructions <br>
- Let the carnage ensue


## User stories

**As a viewer
I can watch a human and zombie on the playing grid
So that I can be amused**

*Given the means to start the program  
When the user initiates the start  
Then a 4x4 grid is rendered on the screen*  

*Given the means to start the program  
When the user initiates the start  
Then a human is occupying a single square*   

*Given the means to start the program  
When the user initiates the start  
Then a zombie is occupying a single square*

*Given the means to start the program  
When the user initiates the start  
Then the human and zombie are on different squares*

*Given the game set up is in process
When an additional zombie is added
Then it will occupy a new empty square*

**As a viewer
I can watch a human move in a random
So that I can be amused**

*Given a program in progress
When it is time for a new go or turn
Then the human will move 1 pace in a random direction (N, NE, E, SE, S, SW, W, NW)*  

*Given a program in progress
When a human moves into a wall
Then the human will not move on that go*

**As a viewer
I can set the speed of a human
So that I can give them a fighting chance**

*Given a program is starting
When I set the speed of a human
Then all humans will move at this speed*

**As a viewer
I can watch a zombie move towards the human
So that my desire for human demolition by zombies can be incited**

*Given a program in progress
When it is time for a new go or turn
Then the zombie will move 1 pace towards the human*

**As a viewer
I can watch a zombie move catch the human and turn it into a zombie
So that my desire for human demolition by zombies can be satisfied**

*Given a program in progress
When a zombie occupies the same square as the human
Then the human will become a zombie*

**As a viewer
I can trigger the start of the game
So that I can watch the mayhem unfold

*Given a terminal in the correct directory
When I trigger the start of the game
Then I will be asked for:
    - dimensions
    - number of humans
    - number of zombies

* Given I have triggered the start of the game 
When I input the paramaters
Then the game will play out on my screen


