package com.niranjan.classes.simple;

/**
 * Created by Niran0303 on 12/26/2016.
 */
public class BoxCons {
    double length,width,height;
    //polymorphic constructor
    BoxCons(double length,double width,double height){
            this.length=length;
            this.width=width;
            this.height=height;

    }
    BoxCons(double l){
        this.length=this.height=this.width=l;
    }
    double volume(){
        return this.length*this.height*this.width;
    }
}
