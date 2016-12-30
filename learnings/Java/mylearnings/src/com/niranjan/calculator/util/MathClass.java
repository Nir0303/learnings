package com.niranjan.calculator.util;

/**
 * Created by Niran0303 on 12/30/2016.
 */
public class MathClass {


    public static void multNumbers(String s1,String s2){
        double a = Double.parseDouble(s1);
        double b = Double.parseDouble(s2);
        System.out.println("Multiplication of "+a+" and "+b +" is "+(a*b));
    }
    public static void subtractNumbers(String s1,String s2){
        double a = Double.parseDouble(s1);
        double b = Double.parseDouble(s2);
        System.out.println("Subtract of "+a+" and "+b +" is "+(a-b));
    }
    public static void addNumbers(String s1,String s2){
        double a = Double.parseDouble(s1);
        double b = Double.parseDouble(s2);
        System.out.println("Addition of "+a+" and "+b +" is "+(a+b));
    }
    public static void divideNumbers(String s1,String s2){
        double a = Double.parseDouble(s1);
        double b = Double.parseDouble(s2);
        System.out.println("Division of "+a+" and "+b +" is "+(a/b));
    }
}
