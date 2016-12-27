package com.niranjan.overriding.figure;

/**
 * Created by Niran0303 on 12/27/2016.
 */
public class FigureRun {
    public static void main(String args[]){
        Figure fig=new Figure(12,232);
        Figure rect=new Rectangle(12,123);
        Figure triangle=new Triangle(12,123);
        Figure a;
        a=fig;
        System.out.println(a.area());
        a=rect;
        System.out.println(a.area());
        a=triangle;
        System.out.println(a.area());
    }
}
