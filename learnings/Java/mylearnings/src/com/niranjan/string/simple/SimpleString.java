package com.niranjan.string.simple;

/**
 * Created by Niran0303 on 12/26/2016.
 */
public class SimpleString {
    public static void main(String args[]){
        String s1="Hi there";
        String s2="Have a good day";
        String s3=s1;
        if (s1.equals(s2)){
            System.out.println("Both strings are equal");
        }
        else{
            System.out.println("Both strings are not equal");
        }

        if(s1.equals(s3)){
            System.out.println("Both srrings are equal");
        }
        else{
            System.out.println("Both strings are not equal");
        }
        System.out.println(s1.length());
        System.out.println(s1.charAt(5));
    }
}
