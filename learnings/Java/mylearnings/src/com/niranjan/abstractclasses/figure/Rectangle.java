package com.niranjan.abstractclasses.figure;

/**
 * Created by Niran0303 on 12/27/2016.
 */
public class Rectangle extends Figure{
    Rectangle(double a,double b){
        super(a,b);
    }
    double area(){
        return a*b;
    }

}
