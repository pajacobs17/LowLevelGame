from tkinter import *;
import time;
from Sprite import *;

def main():

    tk = Tk();
    tk.title("Game demo");
    canvas = Canvas(tk, width=550, height=400, bd=0, highlightthickness=0);
    canvas.pack();
    tk.update();

    sprite = Sprite(canvas);
    keepGoing = True;
    while keepGoing:
        sprite.draw();

        tk.update_idletasks();
        tk.update();
        #fps
        time.sleep(0.10);
        if(sprite.win()):
            keepGoing = False;
                        
main();
