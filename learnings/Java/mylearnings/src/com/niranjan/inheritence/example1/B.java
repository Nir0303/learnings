package com.niranjan.inheritence.example1;

/**
 * Created by Niran0303 on 12/27/2016.
 */
public class B extends A{
    int k;
    void showk(){
        System.out.println("Value of k is "+k);
    }
    void showsum(){
        System.out.println("Sum of i,j and k is "+(i+j+k));
    }

}