package com.niranjan.overriding.figure;

/**
 * Created by Niran0303 on 12/27/2016.
 */
public class Figure {
    double a,b;
    Figure(double a,double b){
         this.a=a;
        this.b=b;
    }
    double area(){
        System.out.println("Figure is undefined");
        return 0;
    }
}
