package com.niranjan.overload.simple;

/**
 * Created by Niran0303 on 12/26/2016.
 */
public class Testrun {
    public static void main(String[] args){
        simpletest t1=new simpletest();
        System.out.println(t1.test());
        System.out.println(t1.test(2));
        System.out.println(t1.test(2,3));
    }
}
