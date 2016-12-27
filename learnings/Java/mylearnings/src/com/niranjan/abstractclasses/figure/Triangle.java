package com.niranjan.abstractclasses.figure;

/**
 * Created by Niran0303 on 12/27/2016.
 */
public class Triangle extends Figure{
    Triangle(double a,double b){
        super(a,b);
    }
    double area(){
        return (a*b)/2;
    }
}
