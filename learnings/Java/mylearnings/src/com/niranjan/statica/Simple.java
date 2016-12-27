package com.niranjan.statica;

/**
 * Created by Niran0303 on 12/26/2016.
 */
public class Simple {
    static int a;
    static int b=3,c=4;
    static int d=4;
    static{
        a=b+c+d;
    }
    static int dosomething(int t){
        System.out.println("Static block instantiated ");
        return a*b+t*c;
    }

    public static void main(String args[]){
        System.out.println(dosomething(10));
    }
}
