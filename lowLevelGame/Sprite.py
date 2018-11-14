from tkinter import *;

MAX_ACCEL = 5;
#0.01 means that 99% of momentum is maintained each frame
DRAG = 0.03;

class Sprite:
    def __init__(self, canvas):
        self.canvas = canvas;
        self.photo = PhotoImage(file="test.gif");
        self.id = canvas.create_image(245, 100, image=self.photo);

        self.x = 0;
        self.y = 0;
        self.dx = 0;
        self.dy = 0;
        #both direction of movement and the rotation angle of the image
        self.moveAngle = 0;
        
        canvas.bind_all('<KeyPress-Left>', self.move_left);
        canvas.bind_all('<KeyPress-Right>', self.move_right);
        canvas.bind_all('<KeyPress-Up>', self.move_up);
        canvas.bind_all('<KeyPress-Down>', self.move_down);
    
    def checkBounds(self, pos):
        #check bottom bounds
        if(pos[0] < 0):
            #******add later to make the full image stay on the screen using screen size
            self.dx = -self.dx;
            self.x = 0;
        
        if(pos[0] > self.canvas.winfo_width()):
            self.dx = -self.dx;
            self.x = self.canvas.winfo_width();

        if(pos[1] < 0):
            #******add later to make the full image stay on the screen using screen size
            self.dy = -self.dy;
            self.y = 0;
        
        if(pos[1] > self.canvas.winfo_height()):
            self.dy = -self.dy;
            self.y = self.canvas.winfo_height() - 1;

    
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
        self.x += self.dx;

    def move_right(self, event):
        self.dx += 2;
        self.x += self.dx;

    def move_up(self, event):
        self.dy -= 2;
        self.y += self.dy;

    def move_down(self, event):
        self.dy += 2;
        self.y += self.dy;
