package com.niranjan.inheritence.box;

/**
 * Created by Niran0303 on 12/27/2016.
 */
public class BoxImplementation {
    public static void main(String args[]){
        BoxWeight b=new BoxWeight(12.0,12.23,223.23,232.1);
        System.out.println("Volume is "+b.volume());
        BoxWeight cube=new BoxWeight(12.0,12.3);
        System.out.println("Volume is "+cube.volume());
        BoxWeight clone=new BoxWeight(b);
        System.out.println("Volume is "+clone.volume());
    }
}
