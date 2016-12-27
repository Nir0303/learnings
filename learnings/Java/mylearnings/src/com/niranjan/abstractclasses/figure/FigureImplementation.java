package com.niranjan.abstractclasses.figure;

import com.niranjan.stack.Stack;
/**
 * Created by Niran0303 on 12/27/2016.
 */
public class FigureImplementation  {
    public static void main(String args[]) {
        //Figure fig=new Figure(10,15); h

        Rectangle rect = new Rectangle(10, 15);
        Triangle tri = new Triangle(10, 15);
        Figure a;
        a = rect;
        Stack s= new Stack();
        s.push(10);
        System.out.println(s.pop());
        System.out.println("Area of Rectangle is "+a.area());
        a=tri;
        System.out.println("Area of Triangle is "+a.area());
    }
}