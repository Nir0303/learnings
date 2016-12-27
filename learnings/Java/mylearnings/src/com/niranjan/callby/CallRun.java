package com.niranjan.callby;

/**
 * Created by Niran0303 on 12/26/2016.
 */
public class CallRun {
    public static void main(String args[]){
        int i,j;
        i=10;
        j=222;
        Call t=new Call(i,j);
        System.out.println("Values outside function before Call By value "+t.i+" "+t.j);
        t.CallByValue(i,j);
        System.out.println("Values outside function After call by value "+t.i+" "+t.j);
        System.out.println("Values outside function before call by reference "+t.i+" "+t.j);
        t.CallByReference(t);
        System.out.println("Values outside function after call by reference"+t.i+" " +t.j);

    }
}
