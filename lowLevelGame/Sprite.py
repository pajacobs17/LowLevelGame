from tkinter import *;

MAX_ACCEL = 5;
#0.01 means that 99% of momentum is maintained each frame
DRAG = 0.03;

class Sprite:
    #no need for x and y since the canvas element already has them
    def __init__(self, canvas, heightMult, widthMult, pos = [100, 100]):
        self.canvas = canvas;
        self.photo = PhotoImage(file="test.gif");
        self.photo = self.photo.zoom(widthMult, heightMult);
        self.id = canvas.create_image(pos[0], pos[1], image=self.photo);

        self.dx = 0;
        self.dy = 0;
        #both direction of movement and the rotation angle of the image
        self.moveAngle = 0;
        
        canvas.bind_all('<KeyPress-Left>', self.move_left);
        canvas.bind_all('<KeyPress-Right>', self.move_right);
        canvas.bind_all('<KeyPress-Up>', self.move_up);
        canvas.bind_all('<KeyPress-Down>', self.move_down);

    def collidesWith(self, otherSprite):
        pass;
        
    def checkBounds(self, pos):
        #check bottom bounds
        if(pos[0] < 0):
            #******add later to make the full image stay on the screen using screen size
            self.dx = -self.dx;
        
        if(pos[0] > self.canvas.winfo_width()):
            self.dx = -self.dx;


        if(pos[1] < 0):
            #******add later to make the full image stay on the screen using screen size
            self.dy = -self.dy;

        
        if(pos[1] > self.canvas.winfo_height()):
            self.dy = -self.dy;

    def getX(self):
        return self.canvas.coords(self.id)[0];

    def getY(self):
        return self.canvas.coords(self.id)[1];
    
    def win(self):
        pass;
    
    def draw(self):
        #to introduce drag into movement when the key is not being pressed
        self.dy *= (1 - DRAG);
        self.dx *= (1 - DRAG);
        pos = self.canvas.coords(self.id);

        self.checkBounds(pos);
        self.canvas.move(self.id, self.dx, self.dy);

    def move_left(self, event):
        self.dx -= 2;

    def move_right(self, event):
        self.dx += 2;

    def move_up(self, event):
        self.dy -= 2;

    def move_down(self, event):
        self.dy += 2;
