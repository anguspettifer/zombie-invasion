# zombie-invasion

## MVP user stories

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



## Considerations:

1. I am adding the "everybody move" method to the Grid class and that is causing me to make changes to 
row too. tightly coupled?
2. Struggling with the fact that __rows is private but I want to test the state of a specific row following
running the everybody_move method in the grid class. I'm making it public, but only for testing purposes... is this ok??