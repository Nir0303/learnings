package com.niranjan.inheritence.box;

/**
 * Created by Niran0303 on 12/27/2016.
 */
public class Box {
     private double length;
     private double width;
     private double height;
    Box(double length,double height,double width){
        this.length=length;
        this.width=width;
        this.height=height;
    }
    Box(double l){
        this.length=this.height=this.width=l;
    }
    Box(){
        this.length=this.height=this.width=0;
    }
    Box(Box b){
        this.length=b.length;
        this.width=b.width;
        this.height=b.height;
    }
    double volume(){
        return this.length*this.width*this.height;
    }
}
