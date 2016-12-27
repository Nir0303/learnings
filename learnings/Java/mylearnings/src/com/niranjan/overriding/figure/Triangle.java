package com.niranjan.overriding.figure;

/**
 * Created by Niran0303 on 12/27/2016.
 */
public class Triangle extends Figure {
    Triangle(double a, double b){
        super(a,b);
    }
    double area(){
        System.out.println("Area of Triangle is");
        return (a*b)/2;
    }
}
