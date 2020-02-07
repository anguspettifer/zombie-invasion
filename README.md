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



## Considerations:

1. I am adding the "everybody move" method to the Grid class and that is causing me to make changes to 
row too. tightly coupled?
2. Struggling with the fact that __rows is private but I want to test the state of a specific row following
running the everybody_move method in the grid class. I'm making it public, but only for testing purposes... is this ok??


Origonal design is 
Square -> Row -> Grid

Now I think I want to get rid of Row and just give squares coordinates. 
The big question is, should a square know it's co-ordinates? Or should it just know it's a square and will render. 
I feel that the grid is responsible for coo-rdinate knowledge. 

Thinking of how to display the board is a key and challenging problem
I have a dict of objects with coordinates and I want to say:
for all the coords, render the object relating to those coords, 
For the others. don't. 

pandas has the answer. in fact. lets just render dataframes. They are fine to look at for this purpose.


dependency inversion. A zombie or human should now how it moves
a grid should call the method and provide the right information. 


Very stuck on "conver_if_needed" method in grid
felt like a big decision to make a new class
Feels like it "should" be easier


Out by one error:
- should Display know that it has to add 1 to grid width?
- Or should Human know that it has to subtract one?


SOLID
S: Only one reason to change
Open/closed: - Open for extension, closed for modification

Generally I think I want less (how do I render? questions and more What type am I? questions)