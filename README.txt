Game Loop with a specified frame rate
	- this is handled in the keepGoing loop in main utilizing the time.sleep() function
	
2D surface for game play
	- I used Tkinter for the 2D surface
	
A refresh / update mechanism
	- this is the .draw() function inside the Sprite Class
	
Some type of sprite entity (class or struct preferred)
	- the whole Sprite class
	
Collision-detection
	- test yourself using the arrow keys, "collision" will print out when the two Sprites hit each other
	
Boundary management
	- run a Sprite into the wall, it will "bounce" off the wall due to a negative dx or dy
	
Transformation - translation, rotation, and scaling
	- translation is handled by using the arrow keys to move the Sprite around the page
	- the scaling comes from the heightMult and widthMult parameters passed in when creating a Sprite
	- rotation is demonstrated by pressing the r key