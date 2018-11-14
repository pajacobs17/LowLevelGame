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

    while 1:
        sprite.draw();

        #tk.update_idletasks();
        tk.update()
        time.sleep(0.01);
                        
main();
