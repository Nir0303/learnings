package com.niranjan.example;


/**
 * Created by Niran0303 on 12/30/2016.
 */
public class AutoBoxError {
    public static void main(String args[]){
        Double a=10.0;
        Double b=4.0;
        Double c=Math.sqrt(a*a+b*b);
        System.out.println(c);
        double a1=10.0;
        double b1=4.0;
        double c1=Math.sqrt(a1*a1+b1*b1);
        System.out.println(c1);
    }
}
