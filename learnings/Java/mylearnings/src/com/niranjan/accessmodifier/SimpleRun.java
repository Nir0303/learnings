package com.niranjan.accessmodifier;

/**
 * Created by Niran0303 on 12/26/2016.
 */
public class SimpleRun {
    public static void main(String args[]){
        Simple s=new Simple();
        s.i=1;
        s.j=2;
        //s.c=3 private access modifer error
        s.setc(3);
        //System.out.println(s.c) private access modifier error
        System.out.println(s.getc());
    }
}
