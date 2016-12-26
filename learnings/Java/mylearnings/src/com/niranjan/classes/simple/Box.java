package com.niranjan.classes.simple;

/**
 * Created by Niran0303 on 12/26/2016.
 */
//Simple without constructors . bad class as all values are exposed
public class Box{
    double length,height,width;
    double volume(){
        return length*width*height;
    }


}
