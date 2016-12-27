package com.niranjan.overload.cons;

/**
 * Created by Niran0303 on 12/26/2016.
 */
public class BoxRun {
    public static void main(String args[]){
    Box b0=new Box();
    Box cube=new Box(1);
    Box b3=new Box(1,2,3);
    Box clone=new Box(b3);
    System.out.println("Volume of b0 is "+b0.volume());
        System.out.println("Volume of cube is "+cube.volume());
        System.out.println("Volume of b3 is "+b3.volume());
        System.out.println("Volume of Clone is"+clone.volume());
    }
}
