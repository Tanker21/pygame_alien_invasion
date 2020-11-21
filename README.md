# pygame_alien_invasion

project from Python Crash Course book, by Eric Matthes

In Alien Invasion, the player controls a rocket ship that appears
at the bottom center of the screen.  The player can move the ship
right and left using the arrow keys and shoot bullets using the
spacebar.  When the game begins, a fleet of aliens fills the sky
and movs across and down the screen.  The player shoots and
destroys the aliens.  If the play shoots all the aliens, a new fleet
appears that moves faster than the previous fleet.  If any alien hits
the player's ship or reaches the bottom of the screen, the player
loses a ship.  If the player loses three ships, the game ends.

The file structure of this project is as follows:
alien_invasion.py-the main file, 
  contains the AlienInvasion class, 
  sets the game settings, 
  creates the game screen, 
  instantiates a ship,
  and listens for events (key presses and releases) which control ship movement and firing
  
Settings.py-file containing the initial game settings

ship.py-contains the ship class and manages the ships position and how to draw the ship

bullet.py-contains the Bullet class, and manages the position of all the bullets in the game

alien.py-contains the Alien class,

button.py-creates the 'Play!' button to start a new game

game_stats.py-manages the statistics of the game and session

...
