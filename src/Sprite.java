/**
 *
 * @author paulj
 */

import java.awt.*;
import java.awt.event.KeyEvent;
import java.awt.image.BufferedImage;
import javax.swing.*;
import java.io.*;
import javax.imageio.ImageIO;

public class Sprite {
    private int x;
    private int y;
    private int dx;
    private int dy;
    private int width;
    private int height;
    private Image image;
    
    public Sprite(String src) {
        createImage(src);
    }
    
    public void createImage(String src) {
        //buffered image to ensure it is created before ever being used, try-catch for src not existing
        BufferedImage img;
        try {
            image = ImageIO.read(new File(src));
        }
        catch(IOException e) {
            System.out.println(e.getMessage());
        }
        
        this.height= image.getHeight(null);
        this.width = image.getWidth(null);
        
        //default location of 0,0
        this.x = 0;
        this.y = 0;
    }
    
    public void move() {
        x += dx;
        y += dy;
    }
    
    public void keyPress(KeyEvent ke) {
        int key = ke.getKeyCode();
        
        if(key == KeyEvent.VK_LEFT) {
            dx -= 2;
        }
        if(key == KeyEvent.VK_RIGHT) {
            dx += 2;
        }
        if(key == KeyEvent.VK_UP) {
            dy += 2;
        }
        if(key == KeyEvent.VK_DOWN) {
            dy -= 2;
        }
    }
    
    //getters for every instance variable except image
    public int getX() {
        return x;
    }
    
    public int getY() {
        return y;
    }
    
    public int getDX() {
        return dx;
    }
    
    public int getDY() {
        return dy;
    }
    
    public int getWidth() {
        return width;
    }
    
    public int getHeight() {
        return height;
    }
    
}
