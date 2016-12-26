package com.niranjan.operators.shift;

/**
 * Created by Niran0303 on 12/25/2016.
 */
public class ShiftOper {
    public static void main(String args[]){
        int a=57;
        //right shift operator
        int b;
        b=a<<2;
        System.out.println("Left shift 2 of "+a+" is "+ b);
        b=a>>2;
        System.out.println("Right shift 2 of "+a+" is "+ b);

    }
}
