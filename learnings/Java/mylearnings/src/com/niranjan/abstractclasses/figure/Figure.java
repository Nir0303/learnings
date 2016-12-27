package com.niranjan.abstractclasses.figure;

/**
 * Created by Niran0303 on 12/27/2016.
 */
abstract class Figure {
    double a,b;
    Figure(double x,double y){
        a=x;
        b=y;
    }
    abstract double area();
}
