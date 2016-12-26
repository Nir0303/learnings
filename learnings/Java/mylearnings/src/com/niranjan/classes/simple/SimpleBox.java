package com.niranjan.classes.simple;

public class SimpleBox{
    public static void main(String args[]){
        System.out.println("Hello");
        Box t=new Box();
        t.length=10;
        t.width=10;
        t.height=10;
        System.out.println("Volume is "+t.height*t.length*t.width);
        System.out.println("Volume is "+t.volume());
        BoxCons t2;
        t2 = new BoxCons(10.0,14.4,12.3);
        System.out.println("Volume is "+t2.volume());
        BoxCons cube = new BoxCons(12.0);
        System.out.println("Volume of cube is "+cube.volume());

    }
}
