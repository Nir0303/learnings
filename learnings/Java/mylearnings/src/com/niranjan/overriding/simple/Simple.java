package com.niranjan.overriding.simple;

/**
 * Created by Niran0303 on 12/27/2016.
 */
public class Simple {
    public static void main(String args[]){
        A a= new A();
        B b= new B();
        C c= new C();
        A r;
        r=a;
        r.show();
        r=b;
        r.show();
        r=c;
        r.show();
    }
}
