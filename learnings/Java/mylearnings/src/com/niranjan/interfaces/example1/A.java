package com.niranjan.interfaces.example1;

/**
 * Created by Niran0303 on 12/28/2016.
 */
public class A implements callme {
    public void callmeback(){
        System.out.println("Implements callme interface");
        System.out.println(t);
    }
    void noninterface(){
        System.out.println("Non Interface function");
    }
}
