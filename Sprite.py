from tkinter import *;


#0.01 means that 99% of momentum is maintained each frame
DRAG = 0.03;

#class Sprite:
    # a base class for users to extend or use themselves.
    # has a width and height multiple for the image that's displayed, a position
    # a rotatation num (out of 4), dx, dy, and a canvas that it is a part of
class Sprite:
    #no need for x and y since the canvas element already has them
    #user passes in the canvas it is a part of and the file
    # optional parameters are the location and width and height multiple
    def __init__(self, canvas, file, heightMult = 1, widthMult = 1, pos = [100, 100]):
        #for usage with image recreation and image resizing
        self.heightMult = heightMult;
        self.widthMult = widthMult;
        
        self.canvas = canvas;
        self.rotateNum = 1;
        self.createImage(file, heightMult, widthMult, pos);
        self.originalFile = file;
        self.dx = 0;
        self.dy = 0;
        #both direction of movement and the rotation angle of the image
        self.moveAngle = 0;

        #key bindings for Sprite movement and rotation
        canvas.bind_all('<KeyPress-Left>', self.move_left);
        canvas.bind_all('<KeyPress-Right>', self.move_right);
        canvas.bind_all('<KeyPress-Up>', self.move_up);
        canvas.bind_all('<KeyPress-Down>', self.move_down);
        canvas.bind_all('<r>', self.rotate);

    #creates the image given a filepath, width and height mult and a position
    #for the image
    def createImage(self, image, heightMult, widthMult, pos):
        self.photo = PhotoImage(file=image);
        self.photo = self.photo.zoom(widthMult, heightMult);
        self.id = self.canvas.create_image(pos[0], pos[1], image=self.photo);
        
    #canvas element doesn't support rotating images, so here's my hacky way
    #to do it, have saved images which are rotated and then load them
    #as the player clicks the rotate button (control)
    def rotateImageCheck(self):
        #for standard rotation
        if(self.rotateNum <=2):
            #to handle the test0.gif case
            if(self.rotateNum == 0):
                file = self.originalFile;
            else:
                index = self.originalFile.find(".");
                file = self.originalFile[:index] + str(self.rotateNum) + self.originalFile[index:];
        #reset the counter if the image is at 270 degrees
        if(self.rotateNum == 3):
            self.rotateNum = 0;
            return self.originalFile;
        #otherwise, just get the next file and return that
        else:
            self.rotateNum += 1;
            return file;

    #checks the collision of two sprite using bounding boxes, uses self and the second sprite being
    # passed in as a paramter
    def checkCollision(self, otherSprite):

        #gets the bounding boxes for the self sprite, stores bounds in
        #variables denoting each side
        boundsSelf = self.canvas.bbox(self.id);
        selfLeft = boundsSelf[0];
        selfRight = boundsSelf[2];
        selfTop = boundsSelf[1];
        selfBottom = boundsSelf[3];

        #gets the bounding boxes for the other sprite, stores bounds in
        #variables denoting each side
        boundsOther = otherSprite.canvas.bbox(otherSprite.id);
        otherLeft = boundsOther[0];
        otherRight = boundsOther[2];
        otherTop = boundsOther[1];
        otherBottom = boundsSelf[3];
        
        collision = True;
        #if the sprites are not colliding, collision is false
        if((selfBottom < otherTop) or (selfTop > otherBottom) or (selfRight < otherLeft) or (selfLeft > otherRight)):
            collision = False;

        return collision;

    #checks whether or not an image is at the bounds. If it is, then
    #set dx, or dy, to -dx or dy depending upon the situation
    def checkBounds(self, pos):
        #check left
        if(pos[0] < 0):
            self.dx = -self.dx;

        #checks the right bound
        if(pos[0] > self.canvas.winfo_width()):
            self.dx = -self.dx;

        #checks the top bounds
        if(pos[1] < 0):
            self.dy = -self.dy;
        
        #checks the bottom bound
        if(pos[1] > self.canvas.winfo_height()):
            self.dy = -self.dy;

    #getter for self.ID
    def getID(self):
        return self.id;

    #getter for x
    def getX(self):
        return self.canvas.coords(self.id)[0];

    #getter for y
    def getY(self):
        return self.canvas.coords(self.id)[1];

    #draws the Sprite, accounting for drag
    def draw(self):
        #to introduce drag into movement when the key is not being pressed
        self.dy *= (1 - DRAG);
        self.dx *= (1 - DRAG);
        pos = self.canvas.coords(self.id);

        self.checkBounds(pos);
        self.canvas.move(self.id, self.dx, self.dy);

    #rotates the image, gets the proper file from rotateImageCheck()
    def rotate(self, event):
        file = self.rotateImageCheck();
        pos = self.canvas.coords(self.id);
        self.createImage(file, self.heightMult, self.widthMult, pos);

    #the functions for handling movement, moves by 2 pixels in the direction of the arrow key presses
    def move_left(self, event):
        self.dx -= 2;

    def move_right(self, event):
        self.dx += 2;

    def move_up(self, event):
        self.dy -= 2;

    def move_down(self, event):
        self.dy += 2;
