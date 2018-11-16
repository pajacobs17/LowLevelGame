from tkinter import *;
import time;
from Sprite import *;

def main():

    tk = Tk();
    tk.title("Game demo");
    canvas = Canvas(tk, width=550, height=400, bd=0, highlightthickness=0);
    canvas.pack();
    tk.update();

    sprite1 = Sprite(canvas, 1, 1, [300, 300]);
    sprite2 = Sprite(canvas, 1, 1, [10, 10]);
    keepGoing = True;
    while keepGoing:
        if(sprite1.collidesWith(sprite2)):
            keepGoing = false;
        sprite1.draw();
        sprite2.draw();

        tk.update_idletasks();
        tk.update();
        #fps
        time.sleep(0.10);
                        
main();
