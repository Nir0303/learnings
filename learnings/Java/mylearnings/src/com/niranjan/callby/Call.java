package com.niranjan.callby;

/**
 * Created by Niran0303 on 12/26/2016.
 */
public class Call {
    int i,j;
    Call(int i,int j){
        this.i=i;
        this.j=j;
    }
    void CallByValue(int i, int j){
        System.out.println("Call By value");
        System.out.println("Value inside function stating"+i+" "+j);
        i*=2;
        j/=2;
        System.out.println("Value inside function after transformation"+i+" "+j);
    }
    void CallByReference(Call c){
        System.out.println("Call bY reference");
        System.out.println("Value inside function stating"+c.i+" "+c.j);
        c.i*=2;
        c.j/=2;
        System.out.println("Value inside function after transformation"+c.i+" "+c.j);
    }
}
