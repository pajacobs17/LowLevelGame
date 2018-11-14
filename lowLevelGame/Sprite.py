from tkinter import *;

class Sprite:
    def __init__(self, canvas):
        self.canvas = canvas;
        self.photo = PhotoImage(file="test.gif");
        self.id = canvas.create_image(245, 100, image=self.photo);

        self.x = 0;
        self.canvas_width = canvas.winfo_width();

        canvas.move(self.id, 200, 300);

        canvas.bind_all('<KeyPress-Left>', self.move_left);
        canvas.bind_all('<KeyPress-Right>', self.move_right);

    def draw(self):
        self.canvas.move(self.id, self.x, 0);
        pos = self.canvas.coords(self.id);

    def move_left(self, event):
        self.x = -2;

    def move_right(self, event):
        self.x = 2;
