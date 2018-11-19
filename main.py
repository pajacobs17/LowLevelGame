#tkinter
from tkinter import *;
#for the fps/update mechanism
import time;
#for getting the Sprite class
from Sprite import *;

def main():
    #creating a TK object, putting a canvas element on it
    tk = Tk();
    tk.title("Game demo");
    canvas = Canvas(tk, width=550, height=400, bd=0, highlightthickness=0);
    canvas.pack();
    tk.update();

    #creating the two sprites using test.gif
    sprite1 = Sprite(canvas, "test.gif", 1, 1, [75, 75]);
    sprite2 = Sprite(canvas, "test.gif", 2, 2, [300, 300]);
    keepGoing = True;

    #loop to run the program, checks for a collision, and updates canvas
    while keepGoing:
        
        if(sprite1.checkCollision(sprite2)):
            print("collision");
        sprite1.draw();
        sprite2.draw();
    
        tk.update_idletasks();
        tk.update();
        #ms delay between frames
        time.sleep(0.10);
                        
main();
