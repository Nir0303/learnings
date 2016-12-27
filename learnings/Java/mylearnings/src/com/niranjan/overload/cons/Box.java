package com.niranjan.overload.cons;

/**
 * Created by Niran0303 on 12/26/2016.
 */
public class Box {
    double length,width,height;
    Box(){
        System.out.println("Empty Box");
       this.length=this.width=this.height=0 ;
    }
    Box(double l){
        System.out.println("Box with all equal sides");
        this.length= this.height=this.width=l;
    }
    Box(double length,double width,double height){
        System.out.println("Box with different sides");
        this.length=length;
        this.height=height;
        this.width=width;
    }
    //passing object instead of primitive values
    Box(Box b){
        System.out.println("Created clone");
        this.width=b.width;
        this.length=b.length;
        this.height=b.height;
    }
    double volume(){
        return this.length*this.height*this.width;
    }
}
