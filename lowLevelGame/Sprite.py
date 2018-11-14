from tkinter import *;

MAX_ACCEL = 5;
DRAG = 0.99;

class Sprite:
    def __init__(self, canvas):
        self.canvas = canvas;
        self.photo = PhotoImage(file="test.gif");
        self.id = canvas.create_image(245, 100, image=self.photo);

        self.x = 0;
        self.y = 0;
        self.dx = 0;
        self.dy = 0;
        print(self.canvas.winfo_height());
        #both direction of movement and the rotation angle of the image
        self.moveAngle = 0;
        #self.canvas_width = canvas.winfo_width();

        canvas.move(self.id, 200, 300);

        canvas.bind_all('<KeyPress-Left>', self.move_left);
        canvas.bind_all('<KeyPress-Right>', self.move_right);
        canvas.bind_all('<KeyPress-Up>', self.move_up);
        canvas.bind_all('<KeyPress-Down>', self.move_down);

        #drag for when keys are released
        #canvas.bind_all('<KeyRelease-Left>', self.release_left);
        #canvas.bind_all('<KeyRelease-Right>', self.release_right);
        #canvas.bind_all('<KeyRelease-Up>', self.release_up);
        #canvas.bind_all('<KeyRelease-Down>', self.release_down);
    """
    def checkBounds(self):
        #check bottom bounds
        if(self.x <= 0):
            pass;
            #self.canvas.move(self.id, self.canvas.winfo_width()/2, self.y);
            #self.y = self.canvas.winfo_width()/2;
            #self.dy = -self.dy;
        if(self.x >= self.canvas.winfo_width()):
            pass;
            #self.canvas.move(self.id, self.canvas.winfo_width()/2, self.y);
            #self.x = self.canvas.winfo_width()/2;
            #self.dy = -self.dy;

        self.canvas.update();
    """
    
    def draw(self):
        self.checkBounds();
        self.dy *= (1 - DRAG);
        self.dx *= (1 - DRAG);
        self.canvas.move(self.id, self.x, self.y);
        pos = self.canvas.coords(self.id);

    def move_left(self, event):
        #to cap acceleration
        if(self.dx > - MAX_ACCEL):
            self.dx -= 2;
        self.x += self.dx;

    def move_right(self, event):
        if(self.dx < MAX_ACCEL):
            self.dx += 2;
        self.x += self.dx;

    def move_up(self, event):
        if(self.dy < MAX_ACCEL):
            self.dy -= 2;
        self.y += self.dy;

    def move_down(self, event):
        if(self.dy > - MAX_ACCEL):
            self.dy += 2;
        self.y += self.dy;
