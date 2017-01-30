package com.niranjan.fruits;

/**
 * Created by Niran0303 on 1/28/2017.
 */

import com.niranjan.fruits.data.*;

import java.lang.reflect.Constructor;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.TreeSet;

public class FruitMarket {

    HashSet<Fruits> cart;

    {
        cart = new HashSet<>();
        Fruits f=new Fruits(FruitNames.BANANA,"green");
        Class<?>  c = f.getClass();
        Constructor<?>[] constructor = c.getConstructors();
        System.out.println("Number of constructors "+constructor.length);
        cart.add(f );
    }

    public void addCart(FruitNames fruit,String colour){
        cart.add(new Fruits(fruit,colour));
    }

    public void printCart(){
        new Object(){
            public  void open(){
                System.out.println("opening cart list");
            }
        }.open();

        for(Fruits f : cart) {
            System.out.println(f);
        }
    }


    public class Fruits {
        FruitNames fName;
        String colour;
        Fruits(FruitNames fName, String colour) {
            this.fName = fName;
            this.colour = colour;
        }
        public FruitNames getfName() {
            return fName;
        }

        public void setfName(FruitNames fName) {
            this.fName = fName;
        }

        public String getColour() {
            return colour;
        }

        public void setColour(String colour) {
            this.colour = colour;
        }

        public String toString(){
            return "You got "+this.colour+" "+this.fName;
        }




    }
}
