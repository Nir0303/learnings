package com.niranjan.controlstatements;

/**
 * Created by Niran0303 on 12/25/2016.
 */
public class ControlStatements {
    public static void main(String[] args){
        int a=10;
        int b=10;
        //nested if
        if(a>b) {
            System.out.println("A is greater than B");
        }
        else if (a==b){
            System.out.println("B is equal to A");
        }
        else{
            System.out.println("B is greater than A");
        }
        //ternary operator
        int greater=(a>b)?a:(a<b)?b:0;
        System.out.println(greater);
        //switch case
        switch(a){
            case 1: System.out.println("Value is 1");break;
            default: System.out.println("Value is not 1");
        }

    }
}
