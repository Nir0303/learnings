package com.niranjan.inheritence.classoveride;



/**
 * Created by Niran0303 on 12/27/2016.
 */
public class B extends A {

    int i;
    B(int i,int j){
        super.i= i;
        this.i=j;
    }
    void showi(){
        System.out.println("Value of i in A is "+super.i);
        System.out.println("Value of i in B is "+ this.i);
    }
}
