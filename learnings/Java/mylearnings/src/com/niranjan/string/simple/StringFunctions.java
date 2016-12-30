package com.niranjan.string.simple;

/**
 * Created by Niran0303 on 12/29/2016.
 */
public class StringFunctions {
    public static void main(String args[]){
        String s1="Say Hello to winter";
        int len=s1.length();
        System.out.println("length of string is "+len);
        int position=s1.indexOf("winter");
        System.out.println("Position of winter in s1 is "+position);
        String s2=s1.substring(13);
        System.out.println("Substring is "+s2);
        String s3="Hello    ";
        System.out.println(s3+".");
        System.out.println(s3.trim()+".");
    }
}
