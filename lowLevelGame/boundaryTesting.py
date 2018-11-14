from tkinter import *;
import time;


def main():

    tk = Tk();
    tk.title("Game demo");
    canvas = Canvas(tk, width=550, height=400, bd=0, highlightthickness=0);
    canvas.pack();
    tk.update();

    sprite = Sprite(canvas);

    while 1:
        sprite.draw();

        tk.update_idletasks();
        tk.update()
        #fps
        time.sleep(0.10);


class Sprite:
    def __init__(self, canvas):
        self.canvas = canvas;

        self.x = 0;
        self.dx = 0;
        self.y = 0;
        #both direction of movement and the rotation angle of the image
        self.moveAngle = 0;
        #self.canvas_width = canvas.winfo_width();

        canvas.bind_all('<KeyPress-Left>', self.move_left);
        canvas.bind_all('<KeyPress-Right>', self.move_right);

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
        #self.checkBounds();
        self.canvas.move(self.x, self.y);
        #pos = self.canvas.coords(self.id);

    def move_left(self, event):
        #to cap acceleration
        if(self.dx > - MAX_ACCEL):
            self.dx -= 2;
        self.x += self.dx;

    def move_right(self, event):
        if(self.dx < MAX_ACCEL):
            self.dx += 2;
        self.x += self.dx;





main();
